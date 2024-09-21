#-*- coding: utf-8 -*-

# 2023/10/22 埼玉大学，設計工学研究室，長谷川
# Trossen Robotics社のPhantomX Hexapodの脚の可動範囲を描画するプログラム
# 自分はC++を普段書いているため，pythonネイティブの人には見苦しいコードになっているかもしれません．
# また，pythonの文法についてや，プログラムの処理についてかなり細かくコメントを書いています．
# そのため，日本語が読めれば，pythonの文法がわからなくても，なんとなくプログラムの処理がわかると思います（笑）．

# pythonのバージョンは3.6.9，Window10で開発を行っていますが，WSL2をいれて，Ubuntu18.04の仮想環境を作って，そこで開発を行っています．
# 依存しているライブラリは，matplotlib，numpy，tdqmです．
# 実行できない場合は，これらのライブラリをインストールしてください．インストール方法は「python (ライブラリ名) install方法」でググってください．
# （おそらく terminalで $ pip3 install matplotlib numpy tdqm と打てばインストールできるかと思いますが）
# ModuleNotFoundError: No module named 'tkinter' とエラーが出た場合は，tkinterをインストールしてください．
# ( このコマンドで可能です $ sudo apt-get install python3-tk )

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
    ax = fig.add_subplot(1,2,1)
    ax_table = fig.add_subplot(1,2,2)

    # 以下グラフの作成，描画

    # 脚が出せる力のグラフを描画
    hexapod_leg_power = dl.HexapodLegPower()
    hexapod_leg_power.set_step(2.0)
    #hexapod_leg_power.render(fig, ax,X_MIN,X_MAX,Z_MIN,Z_MAX)

    # 脚の可動範囲の近似値を描画
    app_graph = dl.ApproximatedGraphRenderer()
    app_graph.set_draw_additional_line(True)
    app_graph.set_draw_fill(True)
    app_graph.set_alpha(0.5)
    app_graph.set_color('green')
    app_graph.set_min_leg_radius(120)
    app_graph.render(ax,Z_MIN,Z_MAX)

    # 脚を描画
    leg_renderer = dl.HexapodLegRenderer()
    leg_renderer.set_event(fig, ax, ax_table)
    leg_renderer.set_circle(True)
    leg_renderer.set_wedge(True)
    leg_renderer.set_img_file_name("result/img_main.png")   # 左クリックで保存するファイル名を指定

    # マウスがグラフのどこをポイントしているかを示す線を描画する
    mouse_grid_renderer = dl.MouseGridRenderer()
    mouse_grid_renderer.set_event(fig, ax)

    # 脚の可動範囲を描画する
    hexapod_range_of_motion = dl.HexapodRangeOfMotion()
    hexapod_range_of_motion.render_lower_leg_range(ax,'black',1)

    ax.set_xlim(X_MIN, X_MAX)   # x 軸の範囲を設定
    ax.set_ylim(Z_MIN, Z_MAX)   # z 軸の範囲を設定

    ax.set_xlabel('x [mm]')        # x軸のラベルを設定
    ax.set_ylabel('z [mm]')        # y軸のラベルを設定

    ax.set_aspect('equal')  # x,y軸のスケールを揃える

    ax.plot([X_MIN,X_MAX],[-25,-25])               # グラフを描画する

    plt.show()  # 表示する