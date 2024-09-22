
#-*- coding: utf-8 -*-

# モジュールのインポート
import matplotlib as mpl
mpl.use('tkagg')
import matplotlib.pyplot as plt

from .hexapod_leg_power import HexapodLegPower
from .hexapod_leg_range_calculator import HexapodLegRangeCalculator
from .approximated_graph_renderer import ApproximatedGraphRenderer
from .hexapod_leg_renderer import HexapodLegRenderer
from .mouse_grid_renderer import MouseGridRenderer
from .hexapod_range_of_motion import HexapodRangeOfMotion
from .hexapod_param import HexapodParam

def display_graph(*, display_table = True,
                  x_min = -100.0, x_max = 300.0, z_min = -200.0, z_max = 200.0,
                  display_leg_power = False, leg_power_step = 2.0,
                  display_approximated_graph = True, set_approx_fill = True, set_approx_color = 'green',
                  set_approx_alpha = 0.5, set_approx_min_leg_radius = 120,
                  set_display_circle = True, set_display_wedge = True, set_display_img_file_name = "result/img_main.png",
                  display_mouse_grid = True, display_ground_line = True, ground_z = -25.0,
                  do_not_show = False):
    '''
    x_min < x < x_max , z_min < z < z_max の範囲でグラフを描画する\n
    変数の値を変更することで処理の内容を変更できる\n

    Parameters
    ----------
    display_table: bool
        表を表示するかどうか
    x_min: float
        x軸の最小値
    x_max: float
        x軸の最大値
    z_min: float
        z軸の最小値
    z_max: float
        z軸の最大値
    display_leg_power: bool
        脚が出せる力のグラフを表示するかどうか
    leg_power_step: float
        何mmごとに力の分布を計算するか
    display_approximated_graph: bool
        脚の可動範囲の近似値を表示するかどうか
    set_approx_fill: bool
        脚の可動範囲の近似値を塗りつぶすかどうか
    set_approx_color: str
        脚の可動範囲の近似値の色
    set_approx_alpha: float
        脚の可動範囲の近似値の透明度
    set_approx_min_leg_radius: float
        脚の可動範囲の近似値の最小半径
    set_display_circle: bool
        脚を円で表示するかどうか
    set_display_wedge: bool
        脚を扇形で表示するかどうか
    set_display_img_file_name: str
        脚を画像で表示する場合の画像ファイル名
    display_mouse_grid: bool
        マウスがグラフのどこをポイントしているかを示す線を表示するかどうか
    display_ground_line: bool
        地面の線を表示するかどうか
    ground_z: float
        地面の高さ
    do_not_show: bool
        show()を実行しないかどうか

    Returns
    -------
    fig : matplotlib.figure.Figure
        グラフのfigure
    ax : matplotlib.axes.Axes
        グラフのaxes
    ax_table : matplotlib.axes.Axes
        表のaxes
    '''

    X_MIN = x_min
    X_MAX = x_max
    Z_MIN = z_min
    Z_MAX = z_max

    if display_table:
        fig = plt.figure()
        ax = fig.add_subplot(1,2,1)
        ax_table = fig.add_subplot(1,2,2)
    else:
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax_table = fig.add_subplot(3,3,2)   # 今回は使用しないので適当な座標に配置
        ax_table.set_visible(False) # 表示しない

    # 以下グラフの作成，描画
    hexapod_pram = HexapodParam()
    hexapod_calc = HexapodLegRangeCalculator(hexapod_pram)

    # 脚が出せる力のグラフを描画
    hexapod_leg_power = HexapodLegPower(hexapod_calc, hexapod_pram, step=leg_power_step)
    if display_leg_power:
        hexapod_leg_power.render(fig, ax, X_MIN, X_MAX, Z_MIN, Z_MAX)

    # 脚の可動範囲の近似値を描画
    app_graph = ApproximatedGraphRenderer(hexapod_calc)
    app_graph.set_draw_additional_line(True)
    app_graph.set_draw_fill(set_approx_fill)
    app_graph.set_alpha(set_approx_alpha)
    app_graph.set_color(set_approx_color)
    app_graph.set_min_leg_radius(set_approx_min_leg_radius)
    if display_approximated_graph:
        app_graph.render(ax, Z_MIN, Z_MAX)

    # 脚を描画
    leg_renderer = HexapodLegRenderer(hexapod_calc, hexapod_pram)
    leg_renderer.set_event(fig, ax, ax_table)
    leg_renderer.set_circle(set_display_circle)
    leg_renderer.set_wedge(set_display_wedge)
    leg_renderer.set_img_file_name(set_display_img_file_name)

    # マウスがグラフのどこをポイントしているかを示す線を描画する
    mouse_grid_renderer = MouseGridRenderer()
    if display_mouse_grid:
        mouse_grid_renderer.set_event(fig, ax)

    # 脚の可動範囲を描画する
    hexapod_range_of_motion = HexapodRangeOfMotion(hexapod_calc, hexapod_pram)
    hexapod_range_of_motion.render_lower_leg_range(ax, 'black', 1.0)

    ax.set_xlim(X_MIN, X_MAX)   # x 軸の範囲を設定
    ax.set_ylim(Z_MIN, Z_MAX)   # z 軸の範囲を設定

    ax.set_xlabel('x [mm]')        # x軸のラベルを設定
    ax.set_ylabel('z [mm]')        # y軸のラベルを設定

    ax.set_aspect('equal')  # x,y軸のスケールを揃える

    if display_ground_line:
        ax.plot([X_MIN, X_MAX], [ground_z, ground_z])               # グラフを描画する

    if not do_not_show:
        plt.show()  # 表示する

    return fig, ax, ax_table
