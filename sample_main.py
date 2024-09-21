
#-*- coding: utf-8 -*-

import phantom_cross as pc

if __name__ == "__main__":
    pc.display_graph()

    pc.display_graph(display_table=False,
                     display_leg_power=False,
                     set_display_circle=False,
                     set_display_wedge=False,
                     set_approx_min_leg_radius=140,
                     display_mouse_grid=False)
