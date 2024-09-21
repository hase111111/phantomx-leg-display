#-*- coding: utf-8 -*-

# 2023/10/22 埼玉大学，設計工学研究室，長谷川
# Trossen Robotics社のPhantomX Hexapodの脚の可動範囲を描画するプログラム
# 自分はC++を普段書いているため，pythonネイティブの人には見苦しいコードになっているかもしれません．
# また，pythonの文法についてや，プログラムの処理についてかなり細かくコメントを書いています．
# そのため，日本語が読めれば，pythonの文法がわからなくても，なんとなくプログラムの処理がわかると思います（笑）．

# pythonのバージョンは3.6.9，Window10で開発を行っていますが，WSL2をいれて，Ubuntu18.04の仮想環境を作って，そこで開発を行っています．
# 依存しているライブラリは，matplotlib，numpy，tdqmです．
# 実行できない場合は，これらのライブラリをインストールしてください．インストール方法は「python (ライブラリ名) install方法」でググってください．
# （おそらく terminalで $ pip3 install matplotlib numpy tdqm と打てばインストールできるかと思いますが）
# ModuleNotFoundError: No module named 'tkinter' とエラーが出た場合は，tkinterをインストールしてください．
# ( このコマンドで可能です $ sudo apt-get install python3-tk )

import phantom_cross as pc

if __name__ == "__main__":
    pc.display_graph()
