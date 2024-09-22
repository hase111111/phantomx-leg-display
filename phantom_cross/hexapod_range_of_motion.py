
#-*- coding: utf-8 -*-

import matplotlib.axes as axes
import matplotlib.pyplot as plt
import numpy as np

from .hexapod_leg_range_calculator import HexapodLegRangeCalculator
from .hexapod_param import HexapodParam

class HexapodRangeOfMotion:

    def __init__(self, hexapod_leg_range_calc: HexapodLegRangeCalculator, hexapod_param: HexapodParam,
                 ax: axes.Axes) -> None:
        self._calc = hexapod_leg_range_calc
        self._param = hexapod_param
        self._ax = ax

        self._STEP = 0.001
        
        # 例外を投げる
        if self._calc == None:
            raise ValueError("hexapod_leg_range_calc is None")
        
        if self._param == None:
            raise ValueError("hexapod_param is None")
        
        if self._ax == None:
            raise ValueError("ax is None")

    def render(self) -> None:
        '''脚の可動範囲を描画する．'''

        print("HexapodLegRangeCalculator.render: Draw the range of motion of the legs")

        self.render_upper_leg_range(self._ax, 'black', 0.3)

        self.render_lower_leg_range(self._ax, 'black', 1.0)

        return

    def render_upper_leg_range(self, color_value: str, alpha_vaule: float) -> None:
        '''
        上脚の可動範囲を描画する．

        Parameters
        ----------
        color_value : str
            色
        alpha_vaule : float
            透明度
        '''

        self._make_leg_range(
            self._param.theta2_min,
            self._param.theta2_max,
            0,
            self._param.theta3_max,
            color_value,
            alpha_vaule
        )


    def render_lower_leg_range(self, color_value: str, alpha_vaule: float) -> None:
        '''
        下脚の可動範囲を描画する．

        Parameters
        ----------
        color_value : str
            色
        alpha_vaule : float
            透明度
        '''

        self._make_leg_range(
            self._param.theta2_min,
            self._param.theta2_max,
            self._param.theta3_min,
            0,
            color_value,
            alpha_vaule
        )

        return

    def _make_leg_range(
            self, theta2_min: float, theta2_max: float, theta3_min: float, theta3_max: float, 
            color_value: str, alpha_vaule: float):
        '''
        脚の可動範囲を描画する．\n
        1つの間接を最大値に固定して,もう一つの間接を最小値から最大値まで動かす．\n
        次に,最小値に固定して,もう一つの間接を最小値から最大値まで動かす．\n
        今度は逆にして描画を行うと,脚の可動範囲が描画できる．

        Parameters
        ----------
        theta2_min : float
            theta2の最小値
        theta2_max : float
            theta2の最大値
        theta3_min : float
            theta3の最小値
        theta3_max : float
            theta3の最大値
        color_value : str
            色
        alpha_vaule : float
            透明度
        '''

        # minからmaxまでstep刻みで配列を作成
        femur_range = np.arange(theta2_min, theta2_max, self._STEP)
        tibia_range = np.arange(theta3_min, theta3_max, self._STEP)

        # femur joint (min ~ max) , tibia joint (min)
        self._make_leg_line(femur_range, [theta3_min], color_value, alpha_vaule)

        # femur joint (min ~ max) , tibia joint (max)
        self._make_leg_line(femur_range,[theta3_max],color_value, alpha_vaule)

        # femur joint (min) , tibia joint (min ~ max)
        self._make_leg_line([theta2_min], tibia_range, color_value,alpha_vaule)

        # femur joint (max) , tibia joint (min ~ max)
        self._make_leg_line([theta2_max], tibia_range, color_value, alpha_vaule)

    def _make_leg_line(self, theta2: list[float], theta3: list[float], color_value: str, alpha_vaule: float) -> None:
        '''
        間接を回しながら，脚先の座標をプロットしていく．

        Parameters
        ----------
        theta2 : list[float]
            theta2の配列
        theta3 : list[float]
            theta3の配列
        color_value : str
            色
        alpha_vaule : float
            透明度
        '''

        line_x = []
        line_z = []

        for i in range(len(theta2)):
            for j in range(len(theta3)):
                res = self._calc.get_leg_position_xz(theta2[i], theta3[j])

                if res[0]:
                    line_x.append(res[1])
                    line_z.append(res[2])

        self._ax.plot(line_x, line_z, color=color_value, alpha=alpha_vaule)
