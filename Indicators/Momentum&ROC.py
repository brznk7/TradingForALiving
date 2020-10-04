# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:56:15 2020

@author: safa
"""

import pandas as pnd
import numpy as np
import datetime as dt
from ExponentialMovingAverage import EMA_Simple
from matplotlib import pyplot as plt

CompanyNames = pnd.read_pickle(r'C:\Users\Dell\Documents\GitHub\TradingForALiving\CompanyNames.pkl')
StockData = pnd.read_pickle(r'C:\Users\Dell\Documents\GitHub\TradingForALiving\CompanyDataDaily.pkl')

SelectedCompany = 'ARCLK'
StartDate = dt.datetime(2019,8,7)
StopDate = dt.date.today()

Data = StockData[SelectedCompany]
Dates = Data[StartDate:StopDate].index.values
Closes = Data[StartDate:StopDate]['Close'].values


## MOMENTUM & RATE OF CHANGE
Period = 7
Momentum = list()
ROC = list()
for i in range(Period,Closes.size):
    momentum = Closes[i] - Closes[i-Period]
    Momentum.append(momentum) 
    
    roc = Closes[i]/Closes[i-Period]*100
    ROC.append(roc)
Momentum = np.array(Momentum)
ROC = np.array(ROC)

## SMOOTHED RATE OF CHANGE
# 13 day EMA of Closes
Period = 13
CloseEMA = EMA_Simple(Closes,13)
# 21 day of ROC
SROC = list()
Period = 21
for i in range(Period,CloseEMA.size):
    sroc = CloseEMA[i]/CloseEMA[i-Period]*100
    SROC.append(sroc)
SROC = np.array(SROC)


fig,axs = plt.subplots(nrows=3, sharex=True)
axs[0].plot(Dates,Closes,label='Close')
axs[0].grid()
axs[0].legend()

axs[1].plot(Dates[Dates.size-Momentum.size:],Momentum,label='Momentum 7 days')
axs[1].grid()
axs[1].legend()
axs[1].axhline(y=0, color='k')

axs[2].plot(Dates[Dates.size-ROC.size:],ROC,label='RoC 7 days')
axs[2].plot(Dates[Dates.size-SROC.size:],SROC,label='S-RoC 21 days')
axs[2].grid()
axs[2].legend()
axs[2].axhline(y=100, color='k')
    