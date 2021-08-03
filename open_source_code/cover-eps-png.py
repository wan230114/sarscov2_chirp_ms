#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-07-31, 12:39:40
# @ Modified By: Chen Jun  
# @ Last Modified: 2021-07-31, 12:44:51  
#############################################

# %%
import os
from PIL import Image


for file in os.popen('find . -type f -name "*.eps"').read().strip().split("\n"):
    newfile = os.path.splitext(file)[0]+".png"
    print(file, "-->", newfile)
    im = Image.open(file)
    im.save(newfile, "PNG")
