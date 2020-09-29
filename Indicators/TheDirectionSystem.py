# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:34:25 2020

@author: Dell
"""

import pandas as pnd
import datetime as dt
from ExponentialMovingAverage import EMA_Simple,SMA
import numpy as np

CompanyNames = pnd.read_pickle('CompanyNames.pkl')
StockData = pnd.read_pickle('CompanyDataUpdated.pkl')

SelectedCompany = 'AEFES'
StartDate = dt.datetime(2019,8,7)
StopDate = dt.datetime(2020,8,7)

Data = StockData[SelectedCompany]
Dates = Data[StartDate:StopDate].index.values
Highs = Data.loc[StartDate:StopDate]['High'].values
Lows = Data.loc[StartDate:StopDate]['Low'].values
Closes = Data.loc[StartDate:StopDate]['Close'].values

DMPos_Array = list()
DMNeg_Array = list()
TR_Array = list()
DIPos_Array = list()
DINeg_Array = list()
for i in range(1,Highs.size): 
    HighToday = Highs[i]
    LowToday = Lows[i]
    HighYest = Highs[i-1]
    LowYest = Lows[i-1]
    CloseYest = Closes[i-1]
    ## Directional Movement 
    if (HighToday-HighYest) > (LowYest-LowToday):
        DM_Pos = max((HighToday-HighYest),0)
    else:
        DM_Pos = 0
        
    if (LowYest-LowToday) > (HighToday-HighYest):
        DM_Neg = max((LowYest-LowToday),0)
    else:
        DM_Neg = 0
    DMPos_Array.append(DM_Pos)
    DMNeg_Array.append(DM_Neg)
    
    ## True Range
    TR_A = abs(HighToday - LowToday)
    TR_B = abs(HighToday - CloseYest)
    TR_C = abs(LowToday - CloseYest)
    TR = max([TR_A,TR_B,TR_C])
    if TR == 0:
        TR = sum(TR_Array[i-4:i])/4
    TR_Array.append(TR)
    
    ## Directional Indicators
    DIPos_Array.append(DM_Pos/TR*100)
    DINeg_Array.append(DM_Neg/TR*100)

TR14 = SMA(TR_Array,14)

DMPos14 = SMA(DMPos_Array,14)
DMNeg14 = SMA(DMNeg_Array,14)

DIPos14 = DMPos14/TR14*100
DINeg14 = DMNeg14/TR14*100

DIDiff = abs(DIPos14-DINeg14)
DISum = DIPos14+DINeg14

DX = DIDiff/DISum*100

#ADX = EMA_Simple(DX,14)
ADX = list()
for i in range(14,DX.size):
    if i == 14:
        adx = DX[:i].sum()/i
        ADX.append(adx)
    else:
        adx = (adx*13+DX[i-1])/14
        ADX.append(adx)
ADX = np.array(ADX)

from matplotlib import pyplot as plt

fig,axs = plt.subplots(nrows=2, sharex=True)
axs[0].plot(Dates,Closes,label='Close')
axs[0].grid()
axs[0].legend()

axs[1].plot(Dates[Closes.size-DIPos14.size:],DIPos14,label='+ DI14',color='green')
axs[1].plot(Dates[Closes.size-DINeg14.size:],DINeg14,label='- DI14',color='red')
axs[1].plot(Dates[Closes.size-ADX.size:],ADX,label='ADX',color='black')
axs[1].grid()
axs[1].legend()



