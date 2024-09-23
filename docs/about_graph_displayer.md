
# GraphDisplayer

GraphDisplayerクラスは，脚の図示を行うクラスです．
GraphDisplayerはdisplayメソッドのみを持ちます．
displayメソッドは多くの引数を持ちますが，デフォルト値が設定されています．
これらを変更することで，脚の図示をカスタマイズできます．

## displayメソッド

### 引数

```python
def display(self, hexapod_pram = HexapodParam(), *, 
            display_table = True,
            display_leg_power = False,
            display_approximated_graph = True,
            display_mouse_grid = True,
            display_ground_line = True,
            display_circle = True, 
            display_wedge = True,
            x_min = -100.0, x_max = 300.0, z_min = -200.0, z_max = 200.0,
            leg_power_step = 2.0,
            approx_fill = True, color_approx = 'green', alpha_approx = 0.5, 
            color_rom = 'black', alpha_upper_rom = 0.3, alpha_lower_rom = 1.0,
            color_mouse_grid = 'black', alpha_mouse_grid = 0.5,
            image_file_name = "result/img_main.png",
            ground_z = -25.0,
            do_not_show = False) -> Tuple[plt.Figure, axes.Axes, axes.Axes]:
```

#### hexapod_pram

HexapodParamクラスのインスタンスを指定します．
HexapodParamクラスは脚ロボットのパラメータを保持しており，
デフォルト値はPhantomX Mk-2のパラメータを持っています．
