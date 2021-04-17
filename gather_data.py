#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:12:02 2021

@author: kadir
"""

import os

os.system('gsutil cp gs://uga-dsp/project3/train.txt .')

f = open('./train.txt').read().split()

for i in f:
    os.system('gsutil cp -r gs://uga-dsp/project3/data/' + i + '.tar .')
    
