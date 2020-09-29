# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:23:20 2020

@author: safa
"""

def MACD(StartDate,StopDate,StockData):
    from ExponentialMovingAverage import EMA_StockData,EMA_OutData
    import pandas as pnd
    from matplotlib import pyplot as plt
   
    ## Calculate 12-day EMA
    Period = 12
    Dates,Closes,EMA12 = EMA_StockData(StockData,StartDate,StopDate,Period)
    
    ## Calculate 26-day EMA
    Period = 26
    Dates,_,EMA26 = EMA_StockData(StockData,StartDate,StopDate,Period)
    
    ## Fast MACD Line
    ## Substract the 26-day EMA from the 12-day EMA
    MACD_Fast = EMA12-EMA26
    MACD_FastFrame = pnd.DataFrame(data = {'Value':MACD_Fast})
    MACD_FastFrame.index = Dates.values
    
    ## Signal MACD Line
    Period = 9
    Dates,_,MACD_Signal = EMA_OutData(StartDate,StopDate,Period,MACD_FastFrame)
    
    ## MACD Histogram
    MACD_Histogram = MACD_Fast - MACD_Signal
    
    fig,axs = plt.subplots(nrows=3, sharex=True)
    axs[0].plot(Dates,Closes,label='Close')
    axs[0].grid()
    axs[0].legend()
    
    axs[1].plot(Dates,MACD_Fast,label='Fast Line')
    axs[1].plot(Dates,MACD_Signal,label='Signal Line')
    axs[1].grid()
    axs[1].legend()
    
    axs[2].bar(Dates,MACD_Histogram,label = 'MACD Histogram')
    axs[2].grid()
    axs[2].legend()