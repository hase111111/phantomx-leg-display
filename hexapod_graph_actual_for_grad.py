#-*- coding: utf-8 -*-

# モジュールのインポート
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
import designlab as dl


# 定数を定義
X_MIN = -100.0
X_MAX = 300.0
Z_MIN = -200.0
Z_MAX = 200.0


if __name__ == "__main__":

    fig = plt.figure()
    ax_table = fig.add_subplot(3,3,2)
    ax = fig.add_subplot(1,1,1)

    ax.plot([X_MIN,X_MAX],[-25,-25], color = "red",linestyle = "dotted")               # グラフを描画する
    #ax.plot([X_MIN,X_MAX],[-50,-50], color = "orange",linestyle = "dotted")               # グラフを

    # 脚の可動範囲の近似値を描画
    app_graph = dl.ApproximatedGraphRenderer()
    app_graph.set_min_leg_radius(130)
    #app_graph.set_draw_fill(False)
    app_graph.set_alpha(0.5)
    app_graph.render(ax,-180, 0.1)

    # 以下グラフの作成，描画

    # 脚が出せる力のグラフを描画
    hexapod_leg_power = dl.HexapodLegPower()
    #hexapod_leg_power.render(fig, ax,X_MIN,X_MAX,Z_MIN,Z_MAX)
    

    # 脚の可動範囲を描画する
    hexapod_range_of_motion = dl.HexapodRangeOfMotion()
    hexapod_range_of_motion.render_lower_leg_range(ax,'black',1)

    x_position = []
    z_position = []

    x_position_first = []
    z_position_first = []
    x_position_second = []
    z_position_second = []
    x_position_end = []
    z_position_end = []

    x_position_first += [131, 131.5, 131.5, 130.5, 132, 133, 134, 130.5, 133, ]
    z_position_first += [-31, -42,   -44,   -52,   -52, -52, -52, -53,   -55, ]

    x_position_first += [131, 132, 133.5, 130.5, 131, 132.5, 130.5, 131.5, 131.5, 132]
    z_position_first += [-60, -61,   -61, -61.5, -63,   -64, -99,   -95,   -94, -92]

    x_position_first += [ 135, 131,  131.5,  133, 130.3, 131,     130.7, 130.5]
    z_position_first += [-110,-118, -117.5, -117, -137.5, -137.5, -139.2,-143]

    x_position_first += [ 131, 134, 130.3, 131,  130, 131.5,]
    z_position_first += [-126, -130, -145,-145, -147,  -146,]

    x_position_first += [  130,  132, 132, 134.5]
    z_position_first += [ -153, -160, -161.5, -160.75]

    x_position_first += [ 131, 130.5]
    z_position_first += [-165, -168]

    x_position_second += [131, 132, 133, 134, 135, 131.5, 132.5, 130]
    z_position_second += [-25, -25, -25, -25, -25,   -25,   -25, -25]

    x_position_end += [  133, 132.5, 134, 134]
    z_position_end += [-63.5,   -76, -85, -99]

    x_position_end += [170,    133,  132,  130.2,  132, 131, 130.5,131.5 ,130,132]
    z_position_end += [-25, -127.5, -145, -166.5, -167, -171, -172.5,-173.5, -173,-173]

    ax.scatter(x_position, z_position, marker = 'o', color = 'orange', s = 20)

    ax.scatter(x_position_second, z_position_second, marker = 'o', color = 'aqua', s = 20)
    ax.scatter(x_position_first, z_position_first, marker = 'o', color = 'darkblue', s = 20)
    ax.scatter(x_position_end, z_position_end, marker = 'o', color = 'blue', s = 20)

    ax.set_xlim(X_MIN, X_MAX)   # x 軸の範囲を設定
    ax.set_ylim(Z_MIN, Z_MAX)   # z 軸の範囲を設定
    ax.set_xlim(50, 250)   # x 軸の範囲を設定
    ax.set_ylim(-200, 0)   # z 軸の範囲を設定

    ax.set_xlabel('x [mm]')     # x軸のラベルを設定
    ax.set_ylabel('z [mm]')     # y軸のラベルを設定

    ax.set_aspect('equal')  # x,y軸のスケールを揃える

    ax_table.set_visible(False)

    plt.show()  # 表示する

    # 画像を保存する
    fig.savefig("result/act_graph.png")