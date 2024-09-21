
#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib.patches as patch
import math

from .hexapod_leg_range_calculator import HexapodLegRangeCalculator

class HexapodLegRenderer:

    _calc = HexapodLegRangeCalculator()

    _WEDGE_R = 20              # 扇形の半径

    _leg_graph = None          # 通常の脚のグラフ
    _error_joint = None        # 範囲外の間接に色をつけるためのグラフ
    _leg_graph_click = None    # クリックされたときに表示する固定されたグラフ
    _angle_table = None        # 角度を表示するためのテーブル
    _femur_circle = None       # 脚の可動範囲を表示するための円
    _tibia_circle = None       # 脚の可動範囲を表示するための円
    _femur_wedge = None        # 脚の角度を表示するための扇形
    _tibia_wedge = None        # 脚の角度を表示するための扇形

    _fig = None

    # [ [coxa x , femur x , tibia x, leg x], [coxa z , femur z , tibia z, leg z] ]の順に格納
    _joint_pos = [[0,0,0,0],[0,0,0,0]]         # 脚の関節の位置
    _joint_pos_click = [[0,0,0,0],[0,0,0,0]]   # クリックされたときに表示するグラフ用

    _alreadly_init = False     # 初期化フラグ
    _reverse = False           # 反転フラグ

    _fig_name = "result/img.png"

    def __init__(self):
        return

    def set_event(self, fig, ax, ax_table):
        '''
        イベントを設定する,初期化処理.2度目以降の呼び出しは無視される\n
        '''

        print("HexapodLegRenderer.set_event : Set the event")

        # すでに初期化済みの場合は何もしない
        if self._alreadly_init:
            print("HexapodLegRenderer.set_event() : Already initialized.")
            return

        # figまたはaxがNoneの場合は何もしない
        if fig == None or ax == None:
            print("HexapodLegRenderer.set_event() : fig or ax is None")
            return

        self._fig = fig

        # 脚の付け根の円を登録
        self._femur_circle = plt.Circle([0,0],color='black',fill=False)
        self._tibia_circle = plt.Circle([0,0],color='black',fill=False)

        self._femur_circle.set_radius(self._calc.FEMUR_LENGTH)    #半径を設定
        self._tibia_circle.set_radius(self._calc.TIBIA_LENGTH)

        self._femur_circle.set_alpha(0.1)                          #透明度を設定
        self._tibia_circle.set_alpha(0.1)

        ax.add_artist(self._femur_circle)
        ax.add_artist(self._tibia_circle)

        #角度用の扇形を登録
        self._femur_wedge = patch.Wedge([0,0], self._WEDGE_R, 0, 10)
        self._tibia_wedge = patch.Wedge([0,0], self._WEDGE_R, 0, 10)

        ax.add_artist(self._femur_wedge)
        ax.add_artist(self._tibia_wedge)

        # 脚の描画
        self._leg_graph, = ax.plot(self._joint_pos[0],self._joint_pos[1])
        self._leg_graph.set_linewidth(5)       #太さを変える
        self._leg_graph.set_marker('o')        #点を描画する
        self._leg_graph.set_markersize(10)     #点の大きさを変える

        self._leg_graph_click, = ax.plot(self._joint_pos[0],self._joint_pos[1])
        self._leg_graph_click.set_linewidth(5)       #太さを変える
        self._leg_graph_click.set_marker('o')        #点を描画する
        self._leg_graph_click.set_markersize(10)     #点の大きさを変える
        self._leg_graph_click.set_visible(False)     #非表示にする

        #可動範囲外の間接に色をつけるためのグラフ
        self._error_joint, = ax.plot(self._joint_pos[0],self._joint_pos[1])
        self._error_joint.set_linewidth(0)       #線を消す
        self._error_joint.set_marker('o')        #点を描画する
        self._error_joint.set_markersize(12)     #点の大きさを変える
        self._error_joint.set_color('red')       #色を変える

        # マウスが動いたときに呼び出す関数を設定
        fig.canvas.mpl_connect('motion_notify_event', self._render)

        # マウスが左クリックされたときに呼び出す関数を設定
        fig.canvas.mpl_connect('button_press_event', self._render_click)

        # 角度を表示するためのテーブルを登録
        self._angle_table = ax_table.table(cellText=[
            ["Joint","Angle [deg]"],["coxa",0],["femur",0],["tibia",0],
            ["coxa servo",0],["femur servo",0],["tibia servo",0],
            ["left coxa servo",0],["left femur servo",0],["left tibia servo",0],
            ["right coxa servo",0],["right femur servo",0],["right tibia servo",0]
            ],loc='center')
        ax_table.axis('off')
        ax_table.axis('tight')

        # 初期化済みフラグを立てる
        self._alreadly_init = True

        return

    def _render(self, event):

        # マウスポイント地点を取得
        mouse_x = event.xdata
        mouse_z = event.ydata

        if mouse_x == None or mouse_z == None:
            # マウスポイント地点が取得できなかった場合は何もしない
            return

        # 脚の角度を計算
        res,self._joint_pos,angle = self._calc.calc_inverse_kinematics_xz(mouse_x, mouse_z, self._reverse)
        self._leg_graph.set_data(self._joint_pos)
        self._leg_graph.set_visible(True)

        # 脚の付け根の円を描画
        self._femur_circle.center = [self._joint_pos[0][1],self._joint_pos[1][1]]
        self._tibia_circle.center = [self._joint_pos[0][2],self._joint_pos[1][2]]

        # 扇形を描画
        self._femur_wedge.set_center([self._joint_pos[0][1],self._joint_pos[1][1]])
        self._femur_wedge.set_theta1(min([0, math.degrees(angle[1])]))
        self._femur_wedge.set_theta2(max([0, math.degrees(angle[1])]))

        self._tibia_wedge.set_center([self._joint_pos[0][2],self._joint_pos[1][2]])
        self._tibia_wedge.set_theta1(min([math.degrees(angle[1]), math.degrees(angle[1] + angle[2])]))
        self._tibia_wedge.set_theta2(max([math.degrees(angle[1]), math.degrees(angle[1] + angle[2])]))


        # 失敗しているならば色を変える
        if res:
            self._leg_graph.set_color('blue')

            #可動範囲外ならばそのプロットの色を変える
            if not self._calc.is_theta2_in_range(angle[1]) or not self._calc.is_theta3_in_range(angle[2]):

                error_point = [[],[]]

                if not self._calc.is_theta2_in_range(angle[1]):
                    error_point[0].append(self._joint_pos[0][1])
                    error_point[1].append(self._joint_pos[1][1])

                if not self._calc.is_theta3_in_range(angle[2]):
                    error_point[0].append(self._joint_pos[0][2])
                    error_point[1].append(self._joint_pos[1][2])

                self._error_joint.set_visible(True)
                self._error_joint.set_data(error_point)

            else:
                self._error_joint.set_visible(False)
        else:
            self._leg_graph.set_color('red')

        # 表を更新
        self._angle_table._cells[(1,1)]._text.set_text("{:.3f}".format(math.degrees(angle[0])))
        self._angle_table._cells[(2,1)]._text.set_text("{:.3f}".format(math.degrees(angle[1])))
        self._angle_table._cells[(3,1)]._text.set_text("{:.3f}".format(math.degrees(angle[2])))

        ar_a,ar_s,ar_ls,ar_rs = self._calc.calc_inverse_kinematics_xz_arduino(mouse_x, -mouse_z)
        self._angle_table._cells[(4,1)]._text.set_text(str(ar_s[0]))
        self._angle_table._cells[(5,1)]._text.set_text(str(ar_s[1]))
        self._angle_table._cells[(6,1)]._text.set_text(str(ar_s[2]))

        table_error_color = 'red'
        table_normal_color = 'white'

        self._angle_table._cells[(7,1)]._text.set_text(str(ar_ls[0]) + " (226 ~ 789)")
        if ar_ls[0] < 226 or ar_ls[0] > 789:
            self._angle_table._cells[(7,1)].set_facecolor(table_error_color)
        else:
            self._angle_table._cells[(7,1)].set_facecolor(table_normal_color)

        self._angle_table._cells[(8,1)]._text.set_text(str(ar_ls[1]) + " (156 ~ 858)")
        if ar_ls[1] < 156 or ar_ls[1] > 858:
            self._angle_table._cells[(8,1)].set_facecolor(table_error_color)
        else:
            self._angle_table._cells[(8,1)].set_facecolor(table_normal_color)

        self._angle_table._cells[(9,1)]._text.set_text(str(ar_ls[2]) + " (272 ~ 859)")
        if ar_ls[2] < 272 or ar_ls[2] > 859:
            self._angle_table._cells[(9,1)].set_facecolor(table_error_color)
        else:
            self._angle_table._cells[(9,1)].set_facecolor(table_normal_color)

        self._angle_table._cells[(10,1)]._text.set_text(str(ar_rs[0]) + " (223 ~ 789)")
        if ar_rs[0] < 223 or ar_rs[0] > 789:
            self._angle_table._cells[(10,1)].set_facecolor(table_error_color)
        else:
            self._angle_table._cells[(10,1)].set_facecolor(table_normal_color)

        self._angle_table._cells[(11,1)]._text.set_text(str(ar_rs[1]) + " (156 ~ 860)")
        if ar_rs[1] < 156 or ar_rs[1] > 860:
            self._angle_table._cells[(11,1)].set_facecolor(table_error_color)
        else:
            self._angle_table._cells[(11,1)].set_facecolor(table_normal_color)

        self._angle_table._cells[(12,1)]._text.set_text(str(ar_rs[2]) + " (157 ~ 743)")
        if ar_rs[2] < 157 or ar_rs[2] > 743:
            self._angle_table._cells[(12,1)].set_facecolor(table_error_color)
        else:
            self._angle_table._cells[(12,1)].set_facecolor(table_normal_color)

        # グラフを再描画
        plt.draw()
        return

    def _render_click(self,event):

        left_click_index = 1
        middle_click_index = 2
        right_click_index = 3

        # 右クリックされた場合は表示を消す
        if event.button == right_click_index:
            self._leg_graph_click.set_visible(False)

        # 中クリックされた場合は反転
        elif event.button == middle_click_index:
            self._reverse = not self._reverse
            self._render(event)

        # 左クリックされた場合は表示を更新
        elif event.button == left_click_index:
            self._fig.savefig(self._fig_name,transparent=True)
            self._leg_graph_click.set_visible(True)
            self._joint_pos_click = self._joint_pos
            self._leg_graph_click.set_data(self._joint_pos_click)

        plt.draw()
        return

    def set_circle(self, vaild):
        #type : (bool) -> None
        '''
        円を表示するかどうかを設定する

        Parameters
        ----------
        vaild : bool
            円を表示するかどうか
        '''

        if vaild:
            self._femur_circle.set_visible(True)
            self._tibia_circle.set_visible(True)
        else:
            self._femur_circle.set_visible(False)
            self._tibia_circle.set_visible(False)

    def set_wedge(self, vaild):
        #type : (bool) -> None
        '''
        扇形を表示するかどうかを設定する

        Parameters
        ----------
        vaild : bool
            扇形を表示するかどうか
        '''

        if vaild:
            self._femur_wedge.set_visible(True)
            self._tibia_wedge.set_visible(True)
        else:
            self._femur_wedge.set_visible(False)
            self._tibia_wedge.set_visible(False)

    def set_img_file_name(self, file_name):
        #type : (str) -> None
        '''
        画像を保存するときのファイル名を設定する

        Parameters
        ----------
        file_name : str
            画像を保存するときのファイル名
        '''

        self._fig_name = file_name
