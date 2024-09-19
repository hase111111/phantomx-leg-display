#-*- coding: utf-8 -*-

# モジュールのインポート
import matplotlib.pyplot as plt
import numpy as np

from .hexapod_leg_range_calculator import HexapodLegRangeCalculator

class ApproximatedGraphRenderer:

    _ax = None
    _Z_MIN = 0
    _Z_MAX = 0
    _GRAPH_STEP = 0.01

    _draw_additional_line = True    #補助線を描画するかどうか 
    _draw_fill = True               #fillするかどうか
    _color = 'green'
    _alpha = 1.0

    _calc = None

    def __init__(self):
        '''
        コンストラクタ pythonでは__init__がコンストラクタになる
        '''
        self._calc = HexapodLegRangeCalculator()  # 計算機のインスタンスを作成

    def render(self,ax,z_min,z_max):
        # type: (plt.axis,float,float) -> None
        '''        
        近似された(Approximated)脚可動範囲の表示を行う．
        セット関数はこの関数の前に呼び出す必要がある

        Parameters
        ----------
        ax : plt.axis
            matplotlibのaxisオブジェクト
        z_min : float
            zの最小値
        z_max : float 
            zの最大値
        '''

        self._ax = ax
        self._Z_MIN = z_min
        self._Z_MAX = z_max

        print("ApproximatedGraphRenderer.render() : Shows approximate leg range of motion")
        print("ApproximatedGraphRenderer.render() : " + 
              "z_min = " + str(self._Z_MIN) + ", " + 
              "z_max = " + str(self._Z_MAX) + ", " +
              "draw_additional_line = " + str(self._draw_additional_line) +  ", " +
              "color = " + self._color +  ", " +
              "alpha = " + str(self._alpha)
        )

        # axがNoneの場合は何もしない
        if self._ax == None:
            print("ax is None")
            return
        
        # z_minとz_maxの大小関係を確認
        if self._Z_MIN > self._Z_MAX:
            print("z_min must be less than z_max")
            return
        
        # 近似された(Approximated)脚可動範囲の計算を行う
        z = np.arange(self._Z_MIN,self._Z_MAX,self._GRAPH_STEP)     # GRAPH_STEP刻みでZ_MINからZ_MAXまでの配列zを作成

        approximated_x_min = np.full_like(z,self._calc.get_approximate_min_leg_raudus())   # xと同じ要素数で値がすべてMIN_LEG_RADIUSの配列zを作成

        approximated_x_max = []
        for i in range(len(z)):
            approximated_x_max.append(self._calc.get_approximate_max_leg_raudus(z[i]))

        if self._draw_additional_line:
            # 補助線を描画する
            self._ax.plot(approximated_x_min, z, color=self._color,alpha=0.1)
            self._ax.plot(approximated_x_max, z, color=self._color,alpha=0.1)

        # xとzで囲まれた範囲をfillする
        if self._draw_fill:
            self._ax.fill_betweenx(
                z,
                approximated_x_min,
                approximated_x_max,
                where=approximated_x_max>=approximated_x_min,
                color=self._color,
                alpha=self._alpha
            )  
        else:
            self._ax.plot(approximated_x_min, z, color=self._color,alpha=self._alpha)
            self._ax.plot(approximated_x_max, z, color=self._color,alpha=self._alpha)

    def set_draw_additional_line(self,draw_additional_line):
        # type: (bool) -> None
        '''
        補助線を描画するかどうかを設定する

        Parameters
        ----------
        draw_additional_line : bool
            補助線を描画するかどうか
        '''
        self._draw_additional_line = draw_additional_line
    
    def set_draw_fill(self,draw_fill):
        # type: (bool) -> None
        '''
        fillするかどうかを設定する

        Parameters
        ----------
        draw_fill : bool
            fillするかどうか
        '''
        self._draw_fill = draw_fill

    def set_color(self,color):
        # type: (str) -> None
        '''
        色を設定する

        Parameters
        ----------
        color : str
            色
        '''
        self._color = color

    def set_alpha(self,alpha):
        # type: (float) -> None
        '''
        透明度を設定する

        Parameters
        ----------
        alpha : float
            透明度
        '''
        self._alpha = alpha

    def set_min_leg_radius(self,min_leg_radius):
        # type: (float) -> None
        '''
        脚の最小半径を設定する

        Parameters
        ----------
        min_leg_radius : float
            脚の最小半径
        '''
        self._calc.set_approximate_min_leg_raudus(min_leg_radius)

if __name__ == "__main__":
    
    print("近似された脚可動範囲の表示を行う")

    # 以下グラフの作成，描画
    fig,ax = plt.subplots()
    
    app_graph = ApproximatedGraphRenderer()
    
    app_graph.render(ax,-200,100)
    
    ax.set_xlim(-100,300)
    ax.set_ylim(-300,300)
    
    plt.show()  # 表示する