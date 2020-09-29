# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:01:44 2020

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
Highs = Data['High'].values
Lows = Data['Low'].values
Closes = Data['Close'].values
Opens = Data['Open'].values
Volumes = Data['Volume'].values

A_D = list()
a_d = 0
for i in range(1,Closes.size):
    Open = Opens[i]
    Close = Closes[i]
    High = Highs[i]
    Low = Lows[i]
    Volume = Volumes[i]
    if High != Low:
        cmfv = (Close-Open)/(High-Low)*Volume
#        cmfv = ((Close-Low)-(High-Close))/(High-Low)*Volume
    a_d = a_d + cmfv
    A_D.append(a_d)
A_D = np.array(A_D)    
    
fig,axs = plt.subplots(nrows=2, sharex=True)
axs[0].plot(Dates,Closes,label='Close')
axs[0].grid()
axs[0].legend()

axs[1].plot(Dates[Dates.size-A_D.size:],A_D,label='Accumulation & Distribution')
axs[1].grid()
axs[1].legend()
axs[1].axhline(y=0, color='k')

