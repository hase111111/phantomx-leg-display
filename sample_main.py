
#-*- coding: utf-8 -*-

# Copyright 2023 Taisei Hasegawa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the “Software”), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
# LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This is a sample code to display the phantom cross graph.

import phantom_cross as pc

if __name__ == "__main__":
    # Display the phantom cross graph.
    pc.display_graph()

    # Display the phantom cross graph without displaying the table and the legend of the power.
    pc.display_graph(display_table=False,
                     display_leg_power=True,
                     leg_power_step=1.0,
                     set_display_circle=False,
                     set_display_wedge=False,
                     set_approx_min_leg_radius=140,
                     display_mouse_grid=False)
