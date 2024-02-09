#-*- coding: utf-8 -*-

# モジュールのインポート
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
import designlab as dl
import pandas as pd


# 定数を定義
X_MIN = -100.0
X_MAX = 300.0
Z_MIN = -200.0
Z_MAX = 200.0


if __name__ == "__main__":

    fig = plt.figure()
    ax_table = fig.add_subplot(3,3,2)   # 今回は使用しないので適当な座標に配置
    ax = fig.add_subplot(1,1,1)

    ax.plot([X_MIN,X_MAX],[-20,-20], color = "red",linestyle = "dotted")               # グラフを描画する

    # 以下グラフの作成，描画

    # 脚が出せる力のグラフを描画
    hexapod_leg_power = dl.HexapodLegPower()
    #hexapod_leg_power.render(fig, ax,X_MIN,X_MAX,Z_MIN,Z_MAX)

    # 脚の可動範囲の近似値を描画
    app_graph = dl.ApproximatedGraphRenderer()
    #app_graph.set_draw_fill(False)
    app_graph.set_alpha(0.5)
    app_graph.render(ax,-183.1, 0.1)

    # 脚を描画
    leg_renderer = dl.HexapodLegRenderer()
    leg_renderer.set_event(fig, ax, ax_table)
    leg_renderer.set_circle(False)
    leg_renderer.set_wedge(False)
    leg_renderer.set_img_file_name("result/img_simu.png")   # 左クリックで保存するファイル名を指定

    # 脚の可動範囲を描画する
    hexapod_range_of_motion = dl.HexapodRangeOfMotion()
    hexapod_range_of_motion.render_lower_leg_range(ax,'black',1)


    # CSVファイルのパス
    csv_file = 'leg/all_simulation_all_leg' + '.csv'

    # CSVファイルを読み込む (x, y, lift, string , error, index)
    data = pd.read_csv(csv_file)

    normal_data = data[data['error'] == True]
    normal_lift_data = normal_data[normal_data['relay'] == True]
    normal_ground_data = normal_data[normal_data['relay'] == False]
    error_data = data[data['error'] == False]

    # グラフを描画する，1列目と，2列目をx, yに指定
    ax.scatter(normal_ground_data['x'], normal_ground_data['z'], marker = 'x', color = 'orange', s = 2)
    ax.scatter(normal_lift_data['x'], normal_lift_data['z'], marker = 'o', color = 'blue', s = 2)
    ax.scatter(error_data['x'], error_data['z'], marker = 'x', color = 'black', s = 2)


    ax.set_xlim(X_MIN, X_MAX)   # x 軸の範囲を設定
    ax.set_ylim(Z_MIN, Z_MAX)   # z 軸の範囲を設定

    ax.set_xlabel('x [mm]')        # x軸のラベルを設定
    ax.set_ylabel('z [mm]')        # y軸のラベルを設定

    ax.set_aspect('equal')  # x,y軸のスケールを揃える

    ax_table.set_visible(False) # 表示しない

    plt.show()  # 表示する