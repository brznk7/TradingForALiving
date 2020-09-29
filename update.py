# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:41:40 2020

@author: safa
"""

import pandas as pnd
import yfinance as yf


CompanyNames = pnd.read_pickle('CompanyNames.pkl')

StockDataDaily = dict()
StockDataWeekly = dict()
for name in CompanyNames:
    data1d = yf.download(name+'.IS',interval='1d')
    StockDataDaily[name] = data1d

pnd.to_pickle(StockDataDaily,'CompanyDataDaily.pkl')
