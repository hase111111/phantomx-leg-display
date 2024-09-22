
#-*- coding: utf-8 -*-

import math

class HexapodParam:
    coxa_length = 52.0     # [mm]
    femur_length = 66.0    # [mm]
    tibia_length = 130.0   # [mm]
    theta1_max = math.radians(81.0)   # [rad]
    theta1_min = math.radians(-81.0)  # [rad]
    theta2_max = math.radians(99.0)   # [rad]
    theta2_min = math.radians(-105)   # [rad]
    theta3_max = math.radians(25.5)   # [rad]
    theta3_min = math.radians(-145.0) # [rad]
    torque_max = 1800.0    # [N*mm] ストールトルク(停動トルク) 
    