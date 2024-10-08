
#-*- coding: utf-8 -*-

# Copyright (c) 2023 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

# Sample code to change robot conditions and display graphs

import math

import phantom_cross as pc


if __name__ == "__main__":
    param = pc.HexapodParam()

    # Change the robot conditions.
    param.coxa_length = 0.0
    param.femur_length = 100.0
    param.tibia_length = 100.0

    param.theta2_max = math.radians(100.0)
    param.theta2_min = math.radians(-100.0)

    param.theta3_max = math.radians(100.0)
    param.theta3_min = math.radians(-100.0)

    # param.torque_max = 1000.0

    # Display the phantom cross graph.
    graph = pc.GraphDisplayer()

    graph.display(
        # use the changed robot conditions.
        param,

        # set display options.
        display_table=False,
        display_circle=False,
        display_wedge=False,
        display_approximated_graph=False,
        display_ground_line=False,
        display_mouse_grid=False,
        # display_leg_power=True,

        # leg_power_step=5.0,

        # set display range.
        x_min=-250.0, x_max=250.0, z_min=-250.0, z_max=250, 

        # set file name to save the image.
        image_file_name="result/sample_main3.png"
        )
