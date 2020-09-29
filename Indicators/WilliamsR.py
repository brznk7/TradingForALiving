# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:19:13 2020

@author: safa
"""

import pandas as pnd
import datetime as dt
from matplotlib import pyplot as plt
import numpy as np

CompanyNames = pnd.read_pickle('CompanyNames.pkl')
StockData = pnd.read_pickle('CompanyDataUpdated.pkl')

SelectedCompany = 'TUKAS'
StartDate = dt.datetime(2019,8,7)
StopDate = dt.datetime(2020,8,7)

Data = StockData[SelectedCompany]

Highs = Data[StartDate:StopDate]['High'].values
Lows = Data[StartDate:StopDate]['Low'].values
Closes = Data[StartDate:StopDate]['Close'].values
Dates = Data[StartDate:StopDate].index.values

Period = 7

WmR = list()
for i in range(Period-1,Closes.size):
    Hr = max(Highs[i-Period+1:i+1])
    Lr = min(Lows[i-Period+1:i+1])
    C = Closes[i]
    
    wmr = 100-(Hr-C)/(Hr-Lr)*100
    WmR.append(wmr)
    
WmR = np.array(WmR)
    
fig,axs = plt.subplots(nrows=2, sharex=True)
axs[0].plot(Dates,Closes,label='Close')
axs[0].grid()
axs[0].legend()

axs[1].plot(Dates[Dates.size-WmR.size:],WmR,label='Williams %R',color='red')
axs[1].grid()
axs[1].legend()
axs[1].axhline(y=90, color='k')
axs[1].axhline(y=10, color='k')

