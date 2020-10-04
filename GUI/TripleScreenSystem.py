# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 16:19:11 2020

@author: safa
"""

def TripleScreenSystem(StockData,StockName,\
                       MACD_StartDate,MACD_StopDate,\
                       Stoch_StartDate,Stoch_StopDate,\
                       MACD_PlotFlag,Stoch_PlotFlag):
    import numpy as np
    from MACD_New import MACD
    from Stochastic import Stochastic
    from OnBalanceVolume import OnBalanceVolume
    from MomentumROC import RoC
    from matplotlib import pyplot as plt
    plt.close('all')

    
    ## Reduce data to weeks
    DataDaily = StockData[StockName].loc[MACD_StartDate:MACD_StopDate]
    Index = np.zeros(DataDaily.shape[0],dtype=bool)
    for i in range(DataDaily.shape[0]-1,0,-5):
        Index[i] = True   
    DataWeekly = DataDaily[Index]
        
    ## Weekly MACD
    Macd,Signal,Histogram=MACD(DataWeekly['Close'].values,DataWeekly.index.values,MACD_PlotFlag)
    
    ## Daily Stochastic
    DataDaily = StockData[StockName].loc[Stoch_StartDate:Stoch_StopDate]
    FastStoc,SlowStock = Stochastic(DataDaily,Stoch_PlotFlag)
    ## Daily Rate of Change
    SRoC = RoC(DataDaily)
    
    
    ## On Balance Volume
    OBV = OnBalanceVolume(DataDaily)
    
    ## PLOT
    DatesDaily = DataDaily.index.values
    ClosesDaily = DataDaily['Close'].values
    DatesWeekly = DataWeekly.index.values
    fig,axs = plt.subplots(nrows=4, sharex=True)
    fig.suptitle(StockName, fontsize=16)
    ## Daily Closes   
    axs[0].plot(DatesDaily,ClosesDaily,label='Daily Close')
    axs[0].grid()
    axs[0].legend()
    ## PLOT MACD
    axs[1].plot(DatesWeekly[25:],Macd,label='Weekly MACD Fast Line')
    axs[1].plot(DatesWeekly[33:],Signal[8:],label='Weekly MACD Signal Line')

    axs[1].bar(DatesWeekly[33:],Histogram[8:],\
               label = 'Weekly MACD Histogram',color='red',linewidth=10)
    ## PLOT ROC
    axs[1].plot(DatesDaily[DatesDaily.size-SRoC.size:],SRoC,label='S-RoC 21 days')
    axs[1].axhline(y=0, color='k')
    axs[1].grid()
    axs[1].legend()

    ## PLOT OBV
    axs[2].plot(DatesDaily[DatesDaily.size-OBV.size:],OBV,label='OBV')
    axs[2].grid()
    axs[2].legend()
    ## PLOT STOCHASTICS
    axs[3].plot(DatesDaily[DatesDaily.size-FastStoc.size:],FastStoc,label='%K Fast')
    axs[3].plot(DatesDaily[DatesDaily.size-SlowStock.size:],SlowStock,label='%D Slow')
    axs[3].grid()
    axs[3].legend()
    axs[3].axhline(y=80, color='k')
    axs[3].axhline(y=20, color='k')
    axs[3].set_ylim(0,100)
    
    ## Set figure position and size
    mngr = plt.get_current_fig_manager()
    mngr.window.setGeometry(250,25,1000,700)
    
    return Macd,Signal,Histogram,FastStoc,SlowStock
    
    
    
       
    
