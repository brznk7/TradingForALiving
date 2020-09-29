# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 19:29:51 2020

@author: safa
"""

import pandas as pnd
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt


CompanyNames = pnd.read_pickle('CompanyNames.pkl')
StockData = pnd.read_pickle('CompanyDataUpdated.pkl')

SelectedCompany = 'AEFES'
StartDate = dt.datetime(2019,2,1)
StopDate = dt.datetime(2020,8,7)

Data = StockData[SelectedCompany]

Data['IndexNum'] = np.arange(0,Data.shape[0])
StartIndex = Data['IndexNum'].loc[StartDate]
StopIndex = Data['IndexNum'].loc[StopDate]
Dates = Data.iloc[StartIndex:StopIndex+1].index
Closes = Data['Close'].iloc[StartIndex:StopIndex+1].values

AveragedClose = list()
N = 10 
for index in range(StartIndex,StopIndex+1):
    SMA = Data['Close'].iloc[index-N:index].values.sum()/N
    AveragedClose.append(SMA)
    
plt.plot(Dates,Closes)
plt.plot(Dates,AveragedClose)
plt.gcf().autofmt_xdate()
plt.grid()