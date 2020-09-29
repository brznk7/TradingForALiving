# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:11:10 2020

@author: safa
"""


def EMA_StockData(StockData,StartDate,StopDate,Period):
    
    import numpy as np
    import pandas as pnd
    
    Data = dict()
    Data['Value'] = StockData['Close'].values
    Data['IndexNum'] = np.arange(0,StockData.shape[0])
    Data = pnd.DataFrame(data = Data)
    Data.index = StockData.index.values
    
    StartIndex = Data['IndexNum'].loc[StartDate]
    StopIndex = Data['IndexNum'].loc[StopDate]
    Dates = Data.iloc[StartIndex:StopIndex+1].index
    DataToAverage = Data['Value'].iloc[StartIndex:StopIndex+1].values
    
    N = Period
    K = 2/(N+1)
    
    AveragedClose = list()
    for i,index in enumerate(range(StartIndex,StopIndex+1)):
        if i <= N:
            SMA = Data['Value'].iloc[index-N:index].values.sum()/N
            AveragedClose.append(SMA)
        elif i == N+1:
            EMA = Data['Value'].iloc[index]*K + SMA*(1-K)
            AveragedClose.append(EMA)
        else:
            EMA = Data['Value'].iloc[index]*K + EMA*(1-K)
            AveragedClose.append(EMA)

    AveragedClose = np.array(AveragedClose)
    return Dates,DataToAverage,AveragedClose

def EMA_OutData(StartDate,StopDate,Period,Data):
    
    import numpy as np

    Data['IndexNum'] = np.arange(0,Data.shape[0])
    
    StartIndex = Data['IndexNum'].loc[StartDate]
    StopIndex = Data['IndexNum'].loc[StopDate]
    Dates = Data.iloc[StartIndex:StopIndex+1].index
    DataToAverage = Data['Value'].iloc[StartIndex:StopIndex+1].values
    
    N = Period
    K = 2/(N+1)
    
    AveragedData = list()
    for i,index in enumerate(range(StartIndex,StopIndex+1)):
        if i <= N:
            SMA = Data['Value'].iloc[index-N:index].values.sum()/N
            AveragedData.append(SMA)
        elif i == N+1:
            EMA = Data['Value'].iloc[index]*K + SMA*(1-K)
            AveragedData.append(EMA)
        else:
            EMA = Data['Value'].iloc[index]*K + EMA*(1-K)
            AveragedData.append(EMA)

    AveragedData = np.array(AveragedData)
        
    return Dates,DataToAverage,AveragedData

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

def SMA(Data,Period):
    import numpy as np
    if isinstance(Data,list):
        Data = np.array(Data)
        
    SmoothedData = list()
    for i in range(Period,Data.size+1):
        if i == Period:
            AveragedData = Data[:Period].sum()
        else:
            AveragedData = AveragedData - (AveragedData/Period) + Data[i-1]
        SmoothedData.append(AveragedData)
    SmoothedData = np.array(SmoothedData)
    return SmoothedData
            
        
            
        
    