
# PhantomX Leg Display

Trossen Robotics社のPhantomX Hexapodの脚の可動域を表示するプログラムです．
卒業研究のために作成したプログラムで，研究の題目は"グラフ探索を用いた多脚ロボットの歩容パターン生成における脚軌道生成失敗時の歩容パターンの再評価手法"です．

## 概要

3関節（yaw - pitch - pitch）の脚を持つ脚ロボットの1脚の可動域を表示するプログラムです．
yaw軸周りの回転は無視し，2次元平面上で表示を行います．
つまり実質的に2リンクのマニピュレータの可動域のように表示します．
グラフや表はmatplotlibを用いて表示しています．

卒業研究のために作成したプログラムのため，Trossen Robotics社の6脚ロボットPhantomX Mk-2の脚のパラメータを用いていますが，パラメータを変更することで他の脚ロボットにも対応可能です．
しかし，間接配置を変更することはできません（yaw-pitch-pitchあるいはyaw-pitchにのみ対応）．

可動範囲のほかに，逆運動学計算による間接角度の算出や，脚先力の算出も行うことができます．
逆運動学は解析解を用いて計算しています．
これらに加えて，実機を動作させるためのサーボモータへの指令値の算出も行うことができます．
また，指令値がサーボモータの可動域を超える場合には，エラーを出力します．

## 使い方

簡単に使用することができるように，パッケージ化しています．
まずは，このレポジトリからインストールしてください．

```bash
pip install git+[このレポジトリのURL]
pip3 install git+[このレポジトリのURL] # Python3の場合

# ex) pip install git+https://github.com/hase111111/phantomx-leg-display.git

# 更新する場合は以下のコマンドを実行してください
# pip install --upgrade git+[このレポジトリのURL] -U
```

インストールが完了したら，以下のコマンドでプログラムを実行してください．
バージョン情報が表示されればインストールは成功です．

```bash
python -m phantom_cross
pyton3 -m phantom_cross  # Python3の場合

# phantom_cross [version]
# This is a package for hexapod robot.
```

### GraphDisplayerクラス

脚の図示はGraphDisplayerクラスを用いて行います．

```python
import phantom_cross as pc

gd = pc.GraphDisplayer()
gd.display()
```

<!--sample_main1.pyを挿入する-->