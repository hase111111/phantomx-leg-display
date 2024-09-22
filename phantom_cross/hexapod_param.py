
#-*- coding: utf-8 -*-

import math

class HexapodParam:
    coxa_length: float = 52.0     # [mm]
    femur_length: float = 66.0    # [mm]
    tibia_length: float = 130.0   # [mm]
    theta1_max: float = math.radians(81.0)   # [rad]
    theta1_min: float = math.radians(-81.0)  # [rad]
    theta2_max: float = math.radians(99.0)   # [rad]
    theta2_min: float = math.radians(-105)   # [rad]
    theta3_max: float = math.radians(25.5)   # [rad]
    theta3_min: float = math.radians(-145.0) # [rad]
    torque_max: float = 1800.0    # [N*mm] ストールトルク(停動トルク) 
    