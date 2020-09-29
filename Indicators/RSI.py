# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 15:39:14 2020

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

#Data = pnd.read_excel('RSI-calculation.xlsx')
#Dates = Data['Date'].values
#Highs = Data['High'].values
#Lows = Data['Low'].values
#Closes = Data['Close'].values


Period = 14
Up = list()
Down = list()
for i in range(1,Closes.size):
    CloseToday = Closes[i]
    CloseYest = Closes[i-1]
    Change = CloseToday - CloseYest
    if Change > 0:
        up = Change
    else:
        up = 0
        
    if Change < 0:
        down = abs(Change)
    else:
        down = 0
    Up.append(up)
    Down.append(down)
    
Up = np.array(Up)
Down = np.array(Down)

UpAve = list()
DownAve = list()
for i in range(Period,Up.size):
    if i == Period:
        upave = Up[i-Period:i].sum()/Period
        downave = Down[i-Period:i].sum()/Period
    else:
        upave = (upave*(Period-1)+Up[i-1])/Period
        downave = (downave*(Period-1)+Down[i-1])/Period
        
    UpAve.append(upave)
    DownAve.append(downave)    
    
UpAve = np.array(UpAve)
DownAve = np.array(DownAve)

RS = UpAve / DownAve
RSI = 100-100/(1+RS)

fig,axs = plt.subplots(nrows=2, sharex=True)
axs[0].plot(Dates,Closes,label='Close')
axs[0].grid()
axs[0].legend()

axs[1].plot(Dates[Dates.size-RSI.size:],RSI,label='RSI')
axs[1].grid()
axs[1].legend()
axs[1].axhline(y=80, color='k')
axs[1].axhline(y=20, color='k')
axs[1].set_ylim(0,100)