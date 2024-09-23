
#-*- coding: utf-8 -*-

# Copyright (c) 2023 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

# Sample code to change robot conditions and display graphs

import matplotlib.pyplot as plt

import phantom_cross as pc


if __name__ == "__main__":
    pc.display_graph(
        # set display options
        display_table=False,
        display_circle=False,
        display_wedge=False,
        display_approximated_graph=False,

        # set file name to save the image
        image_file_name="result/sample_main4.png",

        # do not display the graph
        do_not_show=True
        )

    # Add sample points
    pc._internal_ax.plot([0, 50, 100, 150, 200], [0, 50, 100, 150, 200], "rx")

    # Add a line
    pc._internal_ax.plot([0, 0], [400, 400], "b-")

    # Show the graph
    plt.show()
