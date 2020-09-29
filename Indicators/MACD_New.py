# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:53:29 2020

@author: Dell
"""

def MACD(Closes,Dates,PlotFlag):
    ## EMA
    def EMA(Data,Period):
        import numpy as np
        AveragedData = list()
        for i in range(Data.shape[0]):
            if i == Period-1:
                EMA = Data[i-Period+1:i+1].sum()/Period
            elif i>Period-1:
                EMA=(Data[i]*(2/(Period+1))+EMA*(1-(2/(Period+1))))
            else:
                EMA = 0
            AveragedData.append(EMA)
        AveragedData = np.array(AveragedData)
        return AveragedData
    ## 12 period EMA
    EMA12 = EMA(Closes,12)
    ## 26 period EMA
    EMA26 = EMA(Closes,26)
    ## MACD
    MACD = EMA12[25:]-EMA26[25:]
    ## Signal
    Signal = EMA(MACD,9)
    ## Histogram
    Histogram = MACD-Signal
    
    if PlotFlag == 1:
        from matplotlib import pyplot as plt
        
        fig,axs = plt.subplots(nrows=3, sharex=True)
        axs[0].plot(Dates,Closes,label='Close')
        axs[0].grid()
        axs[0].legend()
        
        axs[1].plot(Dates[25:],MACD,label='Fast Line')
        axs[1].plot(Dates[33:],Signal[8:],label='Signal Line')
        axs[1].grid()
        axs[1].legend()
    
        axs[2].bar(Dates[33:],Histogram[8:],label = 'MACD Histogram')
        axs[2].grid()
        axs[2].legend()
    
    return MACD,Signal,Histogram
    
    
        