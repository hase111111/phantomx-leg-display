#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from .hexapod import HexapodLegRangeCalculator

class HexapodRangeOfMotion:

    _calc = None
    _ax = None
    _STEP = 0.001

    def __init__(self):
        self._calc = HexapodLegRangeCalculator()
        return
    
    def render(self,ax):

        self.render_upper_leg_range(ax,'black',0.3)

        self.render_lower_leg_range(ax,'black',1)

        return
    
    def render_upper_leg_range(self,ax,color_value,alpha_vaule):

        if ax == None:
            return
        
        if self._ax == None:
            self._ax = ax

        self.__make_leg_range(
            HexapodLegRangeCalculator.THETA2_MIN,
            HexapodLegRangeCalculator.THETA2_MAX,
            0,
            HexapodLegRangeCalculator.THETA3_MAX,
            color_value,
            alpha_vaule
        )

        return     
    
    def render_lower_leg_range(self,ax,color_value,alpha_vaule):
        
        if ax == None:
            return
        
        if self._ax == None:
            self._ax = ax

        self.__make_leg_range(
            HexapodLegRangeCalculator.THETA2_MIN,
            HexapodLegRangeCalculator.THETA2_MAX,
            HexapodLegRangeCalculator.THETA3_MIN,
            0,
            color_value,
            alpha_vaule
        )

        return  
    
    def __make_leg_range(self,theta2_min,theta2_max,theta3_min,theta3_max,color_value,alpha_vaule):
        # type: (float,float,float,float,str,float) -> None
        '''
        脚の可動範囲を描画する\n
        1つの間接を最大値に固定して,もう一つの間接を最小値から最大値まで動かす\n
        次に,最小値に固定して,もう一つの間接を最小値から最大値まで動かす\n
        今度は逆にして描画を行うと,脚の可動範囲が描画できる\n

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

        if self._ax == None:
            print("ax is None")
            return
        
        # minからmaxまでstep刻みで配列を作成
        femur_range = np.arange(theta2_min, theta2_max, self._STEP)
        tibia_range = np.arange(theta3_min, theta3_max, self._STEP)

        # femur joint (min ~ max) , tibia joint (min)
        self.__make_leg_line(femur_range,[theta3_min],color_value,alpha_vaule)

        # femur joint (min ~ max) , tibia joint (max)
        self.__make_leg_line(femur_range,[theta3_max],color_value,alpha_vaule)

        # femur joint (min) , tibia joint (min ~ max)
        self.__make_leg_line([theta2_min],tibia_range,color_value,alpha_vaule)

        # femur joint (max) , tibia joint (min ~ max)
        self.__make_leg_line([theta2_max],tibia_range,color_value,alpha_vaule)

    def __make_leg_line(self,theta2,theta3,color_value,alpha_vaule):
        # type: (list[float],list[float],str,float) -> None
        '''
        間接を回しながら，脚先の座標をプロットしていく

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

        if self._ax == None:
            print("ax is None")
            return
        
        line_x = []
        line_z = []

        for i in range(len(theta2)):
            for j in range(len(theta3)):
                res = self._calc.get_leg_position_xz(theta2[i],theta3[j])

                if res[0]:
                    line_x.append(res[1])
                    line_z.append(res[2])

        self._ax.plot(line_x,line_z,color=color_value,alpha=alpha_vaule)

        return