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
    
    
    
    ## PLOT MACD
    Dates = DataWeekly.index.values
    Closes = DataWeekly['Close'].values
    from matplotlib import pyplot as plt
    
    fig,axs = plt.subplots(nrows=3, sharex=True)
    axs[0].plot(Dates,Closes,label='Close')
    axs[0].grid()
    axs[0].legend()
    axs[0].title.set_text('Weekly MACD')

    axs[1].plot(Dates[25:],Macd,label='Fast Line')
    axs[1].plot(Dates[33:],Signal[8:],label='Signal Line')
    axs[1].grid()
    axs[1].legend()

    axs[2].bar(Dates[33:],Histogram[8:],label = 'MACD Histogram')
    axs[2].grid()
    axs[2].legend()
    ## Set figure position and size
    mngr = plt.get_current_fig_manager()
    mngr.window.setGeometry(250,50,1000, 300)
    ## PLOT STOCHASTIC
    Dates = DataDaily.index.values
    Closes = DataDaily['Close'].values
    fig,axs = plt.subplots(nrows=2, sharex=True)
    axs[0].plot(Dates,Closes,label='Close')
    axs[0].grid()
    axs[0].legend()
    axs[0].title.set_text('Daily Stochastic')
    
    axs[1].plot(Dates[Dates.size-FastStoc.size:],FastStoc,label='%D Fast')
    axs[1].plot(Dates[Dates.size-SlowStock.size:],SlowStock,label='%D Slow')
    axs[1].grid()
    axs[1].legend()
    axs[1].axhline(y=80, color='k')
    axs[1].axhline(y=20, color='k')
    axs[1].set_ylim(0,100)
    
    ## Set figure position and size
    mngr = plt.get_current_fig_manager()
    mngr.window.setGeometry(250,400,1000, 300)
    
    return Macd,Signal,Histogram,FastStoc,SlowStock
    
    
    
       
    
