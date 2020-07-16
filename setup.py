#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Created by yu.qi on 2020/07/16.
# Mail:yu.qi@qunar.com

from setuptools import setup, find_packages

install_requires = list(filter(None, ('''
''').splitlines()))

setup(
    name='qiyu_tools',  # 这个是最终打包的文件名
    version='1.0.1',
    entry_points={
        'console_scripts': [
            'mffmpeg = qiyu_tools.mffmpeg:main',
        ],
    },
    url='https://github.com/qiyu/tools',
    maintainer='qiyu',
    maintainer_email='qiyu@souche.com',
    packages=find_packages(),
    package_data={
    },
    install_requires=install_requires
)
