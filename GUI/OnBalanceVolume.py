# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:33:10 2020

@author: safa
"""

def OnBalanceVolume(Data):
    import numpy as np
    
    Closes = Data['Close'].values
    Volumes = Data['Volume'].values
    
    OBV = list()
    obv = 0
    for i in range(1,Closes.size):
        CloseToday = Closes[i]
        CloseYest = Closes[i-1]
        if CloseToday>CloseYest:
            obv = obv + Volumes[i]
        elif CloseToday == CloseYest:
            obv = obv
        elif CloseToday < CloseYest:
            obv = obv - Volumes[i]
        OBV.append(obv)
     
    OBV = np.array(OBV)       
    return OBV       
