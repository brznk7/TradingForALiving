# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 20:26:56 2020

@author: safa
"""

def Stochastic(Data,PlotFlag):
    import numpy as np

    Dates = Data.index.values
    Highs = Data['High'].values
    Lows = Data['Low'].values
    Closes = Data['Close'].values
    
    ## Fast Stochastic %K
    Period = 14
    K = list()
    Hr = list()
    Lr = list()
    C = list()
    for i in range(Period-1,Closes.size):
        hr = max(Highs[i-Period+1:i+1])
        lr = min(Lows[i-Period+1:i+1])
        c = Closes[i]
        
        k = (c-lr)/(hr-lr)*100
        K.append(k)
        Hr.append(hr)
        Lr.append(lr)
        C.append(c)
        
        
        
    K = np.array(K)
    Hr = np.array(Hr)
    Lr = np.array(Lr)
    C = np.array(C)
    
    ## Fast Stochastic %D
    Period = 3
    Dfast = list()
    for i in range(Period-1,K.size):
        d = (C[i-Period+1:i+1]-Lr[i-Period+1:i+1]).sum()/(Hr[i-Period+1:i+1]-Lr[i+1-Period:i+1]).sum()*100
        Dfast.append(d)
       
    Dfast = np.array(Dfast)
    
    ## Slow Stochastic %D
    Period = 3
    Dslow = list()
    for i in range(Period-1,Dfast.size):
        d = Dfast[i-Period+1:i+1].sum()/Period
        Dslow.append(d)
       
    Dslow = np.array(Dslow)
    if PlotFlag == 1:
        from matplotlib import pyplot as plt
        fig,axs = plt.subplots(nrows=2, sharex=True)
        axs[0].plot(Dates,Closes,label='Close')
        axs[0].grid()
        axs[0].legend()
        
        axs[1].plot(Dates[Dates.size-Dfast.size:],Dfast,label='%D Fast')
        axs[1].plot(Dates[Dates.size-Dslow.size:],Dslow,label='%D Slow')
        axs[1].grid()
        axs[1].legend()
        axs[1].axhline(y=80, color='k')
        axs[1].axhline(y=20, color='k')
        axs[1].set_ylim(0,100)
        
    return Dfast,Dslow
    
