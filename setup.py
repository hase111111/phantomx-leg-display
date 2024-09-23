
#-*- coding: utf-8 -*-

# Copyright (c) 2023 Taisei Hasegawa
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

from setuptools import setup, find_packages

setup(
    name='phantom_cross',  # パッケージ名（pip listで表示される）
    version="1.0.1",  # バージョン.
    description="Inverse kinematics of PhantomX and display of results.",  # 説明.
    author='taisei hasegawa',  # 作者名.
    packages=find_packages(),  # 使うモジュール一覧を指定する.
    license='MIT'  # ライセンス.
)
