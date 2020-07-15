#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Created by yu.qi on 2020/07/15.
# Mail:yu.qi@qunar.com

import os
import subprocess

files = os.listdir()
with open('files.txt', 'w') as f:
    f.write('\n'.join(map(lambda file: f"file '{file}'", files)))
subprocess.check_call('ffmpeg -f concat -safe 0 -i files.txt -c copy output.mp4', shell=True)
os.remove('files.txt')
