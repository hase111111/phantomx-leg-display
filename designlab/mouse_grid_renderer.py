
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt

class MouseGridRenderer:

    _alpha = 0.5
    _color = 'black'

    _y_axis = None             # マウスポイント地点を表示するための線
    _x_axis = None             # マウスポイント地点を表示するための線

    _alreadly_init = False     # 初期化フラグ

    def __init__(self):
        return    
    
    def set_event(self,fig,ax):
        # type: (plt.figure,plt.axis) -> None
        '''
        イベントを設定する,2度目以降の呼び出しは無視される\n
        この関数を呼んだ後に,matplotlibのfigureオブジェクトを表示すると,マウスポイント地点を表示するための線が表示される\n
        plt.show()の前に呼び出す,またはこの関数の後にplt.draw()を呼び出す必要がある

        Parameters
        ----------
        fig : plt.figure
            matplotlibのfigureオブジェクト
        ax : plt.axis
            matplotlibのaxisオブジェクト
        '''

        print("MouseGridRenderer.set_event() : マウスグリッドの描画を開始します")

        if self._alreadly_init:
            print("MouseGridRenderer.set_event() : すでに初期化済みです")
            return

        if fig == None or ax == None:
            print("MouseGridRenderer.set_event() : figまたはaxがNoneです")
            return
        
        # マウスポイント地点を表示するための線を登録，
        self._y_axis = ax.axvline(-1)
        self._x_axis = ax.axhline(-1)
   
        self._y_axis.set_linestyle('--')
        self._x_axis.set_linestyle('--')

        self._y_axis.set_alpha(self._alpha)
        self._x_axis.set_alpha(self._alpha)

        self._y_axis.set_color(self._color)
        self._x_axis.set_color(self._color)

        # マウスが動いたときに呼び出す関数を設定
        fig.canvas.mpl_connect('motion_notify_event', self._on_move)  

        self._alreadly_init = True

        return

    def _on_move(self,event):
        
        # マウスポイント地点を取得
        x = event.xdata
        y = event.ydata

        if x == None or y == None:
            # マウスポイント地点が取得できなかった場合は何もしない
            return
        
        # マウスポイント地点を表示するための線の位置を更新
        self._y_axis.set_xdata(x)
        self._x_axis.set_ydata(y)

        return
    
    def set_alpha(self,alpha):
        # type: (float) -> None
        '''
        マウスポイント地点を表示するための線の透明度を設定する\n
        set_event()の前にを呼び出す必要がある

        Parameters
        ----------
        alpha : float
            透明度
        '''

        self._alpha = alpha

        return
    
    def set_color(self,color):
        # type: (str) -> None
        '''
        マウスポイント地点を表示するための線の色を設定する\n
        set_event()の前にを呼び出す必要がある

        Parameters
        ----------
        color : str
            色
        '''

        self._color = color

        return
