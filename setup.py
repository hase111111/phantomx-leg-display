
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='phantom_cross',  # パッケージ名（pip listで表示される）
    version="1.0.0",  # バージョン
    description="Inverse kinematics of PhantomX and display of results.",  # 説明
    author='taisei hasegawa',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT'  # ライセンス
)
