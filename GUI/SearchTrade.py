# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 17:46:34 2020

@author: safa
"""

import pandas as pnd
import datetime as dt
from TripleScreenSystem import TripleScreenSystem

StockData = pnd.read_pickle('CompanyDataDaily.pkl')

MACD_StartDate = dt.datetime(2018,9,14)
MACD_StopDate = dt.datetime(2020,9,18)
ReqRangeSize = pnd.date_range(start=MACD_StartDate,end=MACD_StopDate).size

Stoch_StartDate = dt.datetime(2019,9,14)
Stoch_StopDate = dt.datetime(2020,9,18)

MACD_PlotFlag = 1
Stoch_PlotFlag = 1

StockNames = pnd.read_pickle('CompanyNamesBIST30.pkl')

NameIndex = 5
print(StockNames[NameIndex])
Macd,Signal,Histogram,FastStoc,SlowStoc = TripleScreenSystem(StockData,StockNames[NameIndex],\
                                           MACD_StartDate,MACD_StopDate,\
                                           Stoch_StartDate,Stoch_StopDate,\
                                           MACD_PlotFlag,Stoch_PlotFlag)

#StockToTrade = list()
#StockNotToTrade = list()
#for stockname in StockNames:
#    MACD_PlotFlag = 0
#    Stoch_PlotFlag = 0
#    Macd,Signal,Histogram,FastStoc,SlowStoc = TripleScreenSystem(StockData,stockname,\
#                                               MACD_StartDate,MACD_StopDate,\
#                                               Stoch_StartDate,Stoch_StopDate,\
#                                               MACD_PlotFlag,Stoch_PlotFlag)
#    
#    DataSize = StockData[stockname][MACD_StartDate:MACD_StopDate].shape[0]
#    if StockData[stockname].empty or SlowStoc.size == 0:
#        StockNotToTrade.append(stockname)
#        continue
#    elif Macd[-1] > Signal[-1] and SlowStoc[-1] < 80:
#        MACD_PlotFlag = 1
#        Stoch_PlotFlag = 1
#        StockToTrade.append(stockname)
#    else:
#        StockNotToTrade.append(stockname)
        
        
        
