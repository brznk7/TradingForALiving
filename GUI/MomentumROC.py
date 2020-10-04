# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 15:56:15 2020

@author: safa
"""

def RoC(Data):
    def EMA_Simple(Data,Period):
        
        import numpy as np
        
        if isinstance(Data,list):
            Data = np.array(Data)
        AveragedData = list()
        
        N = Period
        K = 2/(N+1)
        
        AveragedData = list()
        for i in range(N,Data.size):
            if i <= N:
                SMA = Data[i-N:i].sum()/N
                AveragedData.append(SMA)
            elif i == N+1:
                EMA = Data[i]*K + SMA*(1-K)
                AveragedData.append(EMA)
            else:
                EMA = Data[i]*K + EMA*(1-K)
                AveragedData.append(EMA)
    
        AveragedData = np.array(AveragedData)
            
        return AveragedData
    
    import numpy as np
    Closes = Data['Close'].values
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
        sroc = CloseEMA[i]/CloseEMA[i-Period]-1
        SROC.append(sroc)
    SROC = np.array(SROC)
    
    return SROC
    

        