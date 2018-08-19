#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 01:10:20 2018

@author: soubhikdeb
"""

"""
This code is for bit generation in the transport block
"""

import numpy as np

def Bit_generation(tbs):
    Transport_Block = list(np.random.randint(2,size=tbs))
    return Transport_Block