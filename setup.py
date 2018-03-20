# coding:utf8
from setuptools import setup

import trader

long_desc = """
silver-trader
===============

Installation
--------------
pip install silver-trader

Upgrade
---------------
pip install silver-trader --upgrade
"""

setup(
    name='silver-trader',
    version=trader.__version__,
    description='',
    long_description=long_desc,
    author='wuleying',
    author_email='lolooo@live.com',
    license='BSD',
    url='https://github.com/wuleying/silver-trader',
    keywords='',
    install_requires=[
        'requests',
        'pandas'
    ],
    classifiers=[],
    packages=[],
)
