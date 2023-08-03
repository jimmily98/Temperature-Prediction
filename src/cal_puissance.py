# calculate power of a refrigerated container
import numpy as np
import pandas as pd
import os
import sys
import matplotlib.pyplot as plt
import math
import statistics

def cal_puissance(pho, V,c,lamb,s,L, step, step_num, data):
    # pho: density of the material
    # V: volume of the container
    # c: heat capacity
    # lamb: thermal conductivity
    # s: surface area
    # L: thickness of the material
    # step: time interval
    # step_num: the step at which the power is calculated (1,2, ....)
    # data: the dataframe of the temperature data

    # power == average power from (step - 1) to (step + 1)
    delta_T1 = statistics.mean(data.iloc[step_num-1, 14:26].astype(float) - data.iloc[step_num+1, 14:26].astype(float))
    delta_T21 = statistics.mean(np.array(data.iloc[step_num-1, 2:14].astype(float)) - np.array(data.iloc[step_num-1, 14:26].astype(float)))
    delta_T22 = statistics.mean(np.array(data.iloc[step_num, 2:14].astype(float)) - np.array(data.iloc[step_num, 14:26].astype(float)))
    delta_T23 = statistics.mean(np.array(data.iloc[step_num+1, 2:14].astype(float)) - np.array(data.iloc[step_num+1, 14:26].astype(float)))

    m = pho * V
    return (m*c*delta_T1/2/step) + (lamb*s*(delta_T21+2*delta_T22+delta_T23)/4/L)

df = pd.read_excel('F3340.xlsx',decimal=',',header=None)
data = df.iloc[7:, 0:26]
pho = 1.293e-3 # density of air
c = 1.01 # heat capacity of air
step = 120 # time interval (seconds)
power = cal_puissance(pho, 90, c, 0.5, 138, 0.2, step, 10, data)
print("power: ", power)

