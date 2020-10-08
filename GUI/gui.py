# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 11:16:42 2020

@author: safa
"""

import tkinter as tk
from TripleScreenSystem import TripleScreenSystem as TSS
import datetime as dt
import pandas as pnd

StockData = pnd.read_pickle(r'C:\Users\Dell\Documents\GitHub\TradingForALiving\CompanyDataDaily.pkl')
StockNames = pnd.read_pickle(r'C:\Users\Dell\Documents\GitHub\TradingForALiving\CompanyNamesBIST100.pkl')
MACD_StartDate = dt.datetime(2019,7,14)
MACD_StopDate = dt.date.today()

Stoch_StartDate = dt.datetime(2019,7,14)
Stoch_StopDate = dt.date.today()

MACD_PlotFlag = 0
Stoch_PlotFlag = 0

root = tk.Tk()
root.title('Stock2Trade')


List = tk.Listbox(root)

for i,stockname in enumerate(StockNames):
    List.insert(i+1,stockname)

List.grid(row=1,column=0)

RunButton = tk.Button(root,text='Run',command=lambda:TSS(StockData,List.get(tk.ACTIVE),\
                                                       MACD_StartDate,MACD_StopDate,\
                                                       Stoch_StartDate,Stoch_StopDate,\
                                                       MACD_PlotFlag,Stoch_PlotFlag))
RunButton.grid(row=2,column=0)

root.mainloop()

