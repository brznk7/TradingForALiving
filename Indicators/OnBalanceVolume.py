# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:33:10 2020

@author: safa
"""

import pandas as pnd
import datetime as dt
from matplotlib import pyplot as plt
import numpy as np
from ExponentialMovingAverage import EMA_Simple,SMA

CompanyNames = pnd.read_pickle('CompanyNames.pkl')
StockData = pnd.read_pickle('CompanyDataUpdated.pkl')

SelectedCompany = 'AEFES'
StartDate = dt.datetime(2019,8,7)
StopDate = dt.datetime(2020,8,7)

Data = StockData[SelectedCompany][StartDate:StopDate]

Dates = Data.index.values
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
    
fig,axs = plt.subplots(nrows=2, sharex=True)
axs[0].plot(Dates,Closes,label='Close')
axs[0].grid()
axs[0].legend()

axs[1].plot(Dates[Dates.size-OBV.size:],OBV,label='OBV')
axs[1].grid()
axs[1].legend()
