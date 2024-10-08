
#-*- coding: utf-8 -*-

# Copyright (c) 2023 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

# Sample to calculate force distribution.

import phantom_cross as pc


if __name__ == "__main__":
    graph = pc.GraphDisplayer()

    graph.display(
        # set display options.
        display_approximated_graph=False,
        display_leg_power=True,
        display_circle=False,
        display_table=False,
        display_wedge=False,
        display_ground_line=False,

        # set step size of force distribution.
        leg_power_step=5.0,

        # set file name to save the image.
        image_file_name="result/sample_main2.png"
    )

    # By clicking the left mouse button, an image of the leg at that position can be saved.
