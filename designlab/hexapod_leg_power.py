#-*- coding: utf-8 -*-

# モジュールのインポート
import matplotlib as mpl
import matplotlib.pyplot as plt
import copy
import numpy as np
import math
import tqdm

from .hexapod import HexapodLegRangeCalculator

class HexapodLegPower:

    _calc = None
    _ax = None

    _step = 1.0            # 何mmごとに力の分布を計算するか，小さくしすぎると計算時間がかかる

    _TORQUE_MAX = 1800.0   # ストールトルク(停動トルク) [N*mm]

    _PRINT_DEV = int(20)   # 何%ごとに進捗を表示するか. 5%ごとならば，20回に1回表示するため20を指定する

    def __init__(self):
        self._calc = HexapodLegRangeCalculator()
        return
    
    def render(self, fig, ax, x_min, x_max, z_min, z_max):
        # type: (plt.fig ,plt.Axes, float, float, float, float) -> None
        '''
        x_min < x < x_max , z_min < z < z_max の範囲でグラフを描画する\n
        力の大きさは，等高線で表現する\n
        大変時間のかかる処理なので，実行には時間がかかる\n
        '''

        print("HexapodLegPower.render: 力の分布を描画します.時間のかかる処理のため,10秒程度お待ちください.")

        # min < max でない場合は終了する
        if x_min >= x_max:
            print("HexapodLegPower.render: x_min >= x_max")
            return
        
        if z_min >= z_max:
            print("HexapodLegPower.render: z_min >= z_max")
            return

        # 計算機がインスタンス化されていない場合は終了する
        if self._calc == None:
            print("HexapodLegPower.render: self.__calc is None")
            return
        
        # グラフがインスタンス化されていない場合は，axを設定する
        if self._ax == None:
        
            # axがNoneの場合は終了する
            if ax == None: 
                print("HexapodLegPower.render: ax is None")
                return
            
            self._ax = ax

        if fig == None:
            print("HexapodLegPower.render: fig is None")
            return

        # x_min < x < x_max , z_min < z < z_max の範囲でグラフを描画するため，minからmaxまでself.__STEPづつ増やした数値を格納した配列を作成する
        x_range = np.arange(x_min, x_max, self._step)
        z_range = np.arange(z_min, z_max, self._step)

        # x*zの要素数を持つ2次元配列power_arrayを作成する(xが列，zが行)
        power_array = np.zeros((len(z_range),len(x_range)))

        # power_arrayの各要素に,x,zの座標における脚がだせる最大の力を計算して代入する,進捗表示のためにtqdmを使用する.必要なければ普通にrangeを使っても良い
        for i in tqdm.tqdm(range(len(x_range))):
            for j in tqdm.tqdm(range(len(z_range)), leave=False):

                # j→i (z→x) の順で配列を参照することに注意
                power_array[j][i] = self.__get_max_power(x_range[i], z_range[j],0,1)

        # power_arrayを等高線で描画する
        cmap = copy.copy(mpl.cm.get_cmap("jet"))
        cmap.set_under('silver')
        cmap.set_over('silver')
        power_contourf = self._ax.contourf(x_range, z_range, power_array, cmap=cmap, levels=20, vmin=4.0, vmax=20.0)

        # カラーバーを表示する
        cbar = fig.colorbar(power_contourf)
        cbar.set_label("[N]", fontsize=20)
  
        return

    def set_step(self,step):
        # type: (float) -> None
        '''
        何mmごとに力の分布を計算するかを設定する\n
        小さくしすぎると計算時間がかかる\n

        Parameters
        ----------
        step : float
            何mmごとに力の分布を計算するか
        '''

        # stepが1以下の場合は終了する
        if step <= 0:
            print("HexapodLegPower.set_step: step <= 0")
            return

        self._step = step

        return
    
    def __get_max_power(self, x, z, power_x, power_z):
        # type: (float, float, float, float) -> float
        '''
        x,zの座標における脚の力の最大値を返す

        Parameters
        ----------
        x : float
            脚先のx座標 [mm]
        z : float
            脚先のz座標 [mm]
        power_x : float
            x方向にかかる力.正規化されていること [N]
        power_z : float
            z方向にかかる力.正規化されていること [N]

        Returns
        -------
        ans : float
            引数で受け取った力を何倍したら，トルクが最大値を超えるか．\n倍率を返す
        '''

        # 逆運動学解．間接の角度を求める
        is_sucess,joint_pos,angle = self._calc.calc_inverse_kinematics_xz(x, z)

        # 逆運動学解が得られなかった場合は終了する
        if not is_sucess or (is_sucess and (not self._calc.is_theta2_in_range(angle[1]) or not self._calc.is_theta3_in_range(angle[2]))):

            # もう一つの逆運動学解を求める
            is_sucess,joint_pos,angle = self._calc.calc_inverse_kinematics_xz(x, z, True)
            
            if not is_sucess or (is_sucess and (not self._calc.is_theta2_in_range(angle[1]) or not self._calc.is_theta3_in_range(angle[2]))):
                return 0.0
        
        ans = 0

        # 逆運動学解が得られた場合は，トルクの計算をする
        power_list = np.arange(1,20,1)    #6から12までの0.5刻みのリスト
        for p in power_list:

            # ヤコビ行列を作成
            jacobian = self.__make_jacobian(angle[1], angle[2])

            # 力のベクトルを作成 [F_x, F_z]^T
            power = np.matrix(
                [
                    [(float)(power_x * p)],
                    [(float)(power_z * p)]
                ]
            )

            # トルクを計算する [tauqe_femur, tauqe_tibia]^T
            tauqe = np.dot(jacobian.T , power)  # t = J^T * F

            # トルクの絶対値を計算する
            femur_tauqe = math.fabs(tauqe[0][0])
            tibia_tauqe = math.fabs(tauqe[1][0])    

            # トルクの最大値を超えていないか判定する．超えたら終了，超えていなければ記録して次のループへ
            if femur_tauqe < self._TORQUE_MAX and tibia_tauqe < self._TORQUE_MAX:
                ans = p
            else:
                break

        return (float)(ans)

    def __make_jacobian(self, theta2, theta3):
        # type: (float, float) -> np.matrix
        '''
        ヤコビ行列を計算する

        Parameters
        ----------
        theta2 : float
            第2間接の角度 [rad]
        theta3 : float
            第3間接の角度 [rad]

        Returns
        -------

        
        jacobian : np.matrix
            2*2のヤコビ行列
        '''

        # 必要なクラスがインスタンスされてないならば終了する
        if self._calc == None:
            print("HexapodLegPower.__make_jacobian: self.__calc is None")
            return np.matrix([[0,0],[0,0]])
        
        Lf = self._calc.FEMUR_LENGTH
        Lt = self._calc.TIBIA_LENGTH

        # 2*2のヤコビ行列を作成
        jacobian = np.matrix(
            [
                [-Lf * math.sin(theta2) - Lt * math.sin(theta2+theta3), -Lt * math.sin(theta2+theta3)],
                [Lf * math.cos(theta2) + Lt * math.cos(theta2+theta3),  Lt * math.cos(theta2+theta3)]
            ]
        )

        return jacobian