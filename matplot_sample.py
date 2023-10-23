#-*- coding: utf-8 -*-

# モジュールのインポート
import matplotlib.pyplot as plt
import numpy as np
import math
import const
import designlab as dl


# 自作したconst moduleを使って定数を定義
const.X_MIN = 0
const.X_MAX = 250
const.Z_MIN = -200
const.Z_MAX = 100

const.MIN_LEG_RADIUS = 120


const.GRAPH_STEP = 0.01

if __name__ == "__main__":
    
    # 近似された(Approximated)脚可動範囲の計算を行う
    calc = dl.HexapodLegRangeCalculator()  # 計算機のインスタンスを作成

    z = np.arange(const.Z_MIN,const.Z_MAX,const.GRAPH_STEP)  # const.GRAPH_STEP刻みでconst.Z_MINからconst.Z_MAXまでの配列zを作成

    approximated_x_min = np.full_like(z,const.MIN_LEG_RADIUS)             # xと同じ要素数で値がすべてconst.MIN_LEG_RADIUSの配列zを作成

    approximated_x_max = []
    for i in range(len(z)):
        approximated_x_max.append(calc.get_approximate_max_leg_raudus(z[i]))


    # 実際の(Actual)脚可動範囲の計算を行う
    actual_x = []
    actual_z = []
    actual_leg_angle = []   # 脚の角度とx,z座標を格納する配列

    theta2 = np.arange(-math.pi,math.pi,const.GRAPH_STEP)  # const.GRAPH_STEP刻みで-math.piからmath.piまでの配列theta2を作成
    theta3 = np.arange(-math.pi,math.pi,const.GRAPH_STEP)  # 同様に，const.GRAPH_STEP刻みで-math.piからmath.piまでの配列theta3を作成
    #theta3 = np.arange(0,0.01,const.GRAPH_STEP)  # 同様に，const.GRAPH_STEP刻みで-math.piからmath.piまでの配列theta3を作成

    for i in range(len(theta2)):
        for j in range(len(theta3)):
            res = calc.get_leg_position_xz(theta2[i],theta3[j]) # 脚の角度を引数にして，脚のx,z座標を計算する

            if res[0]:  # 脚のx,z座標が計算できた場合
                angle = (theta2[i]+theta3[j]) * -1.0 # 接地面に対する脚の角度

                actual_x.append(res[1])  # 脚の角度とx,z座標を配列に追加
                actual_z.append(res[2])
                actual_leg_angle.append(math.degrees(angle))

    # 以下グラフの作成，描画
    fig,ax = plt.subplots()

    ax.plot(approximated_x_min,z,color='green',alpha=0.1)
    ax.plot(approximated_x_max,z,color='green',alpha=0.1)
    ax.fill_betweenx(z,approximated_x_min,approximated_x_max,where=approximated_x_max>=approximated_x_min,color='green',alpha=0.5)  # xとzで囲まれた範囲をfillする

    #cm = plt.cm.get_cmap('jet') # カラーマップの設定
    mapable = ax.scatter(actual_x,actual_z,alpha=1.0)
    #ax.scatter(actual_x,actual_z,c=actual_leg_angle,alpha=0.1)

    #ax.set_xlim(const.X_MIN,const.X_MAX)   # x 軸の範囲を設定
    #ax.set_ylim(const.Z_MIN,const.Z_MAX)   # z 軸の範囲を設定
    ax.set_xlim(-300,300)
    ax.set_ylim(-300,300)
    ax.set_aspect('equal')

    plt.show()  # 表示する