import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
import streamlit as st

# calculate power of a refrigerated container

# calculate power of a refrigerated container (with K (W/m^2*C))
# q = K*A*T*time

def cal_puissance_n(pho,V,m_isolant,c,c_isolant,K,A,step, step_num, data):
    # pho: density of the material
    # V: volume of the container
    # c: heat capacity
    # K: thermal conductivity, unity: (W/m^2*C)
    # A: internal surface 
    # step: time interval
    # step_num: the step at which the power is calculated (1,2, ....)
    # data: the dataframe of the temperature data

    # power == average power from (step - 1) to (step + 1)
    
    delta_T1 = statistics.mean(data.iloc[step_num-1,12:24].astype(float) - data.iloc[step_num+1,12:24].astype(float))
    delta_T21 = statistics.mean(np.array(data.iloc[step_num-1, 0:12].astype(float)) - np.array(data.iloc[step_num-1, 12:24].astype(float)))
    delta_T22 = statistics.mean(np.array(data.iloc[step_num, 0:12].astype(float)) - np.array(data.iloc[step_num, 12:24].astype(float)))
    delta_T23 = statistics.mean(np.array(data.iloc[step_num+1, 0:12].astype(float)) - np.array(data.iloc[step_num+1, 12:24].astype(float)))

    m = pho * V
    Q1 = m*c*delta_T1 + m_isolant*c_isolant*1000*delta_T1/2
    
    Q2 = K*A*(delta_T21+2*delta_T22+delta_T23)*step/2
    
    
    return Q1/2/step, Q2/2/step, (Q1+Q2)/2/step

### ----------------------- Read Coefficients  -----------------------
prsd = st.button('Display')
if prsd:
    if st.session_state['df_par']==1:
        prts = pd.read_excel("data/EssaiClient.xlsx",decimal='.',header=None)
    else:
        st.chat_message('Please upload your parameters OR use default parameters')
        st.stop()
    essnum = st.session_state['option']
    row = prts[prts[0] == essnum].index[0]
    length = prts[6][row]
    width = prts[7][row]
    height = prts[8][row]
    V = prts[9][row]
    A = prts[10][row]
    Density = prts[12][row]
    c_isolant = prts[13][row]
    L_T = [float(item)/1000 for item in prts[14][row].split(',')]
    L_B = [float(item)/1000 for item in prts[15][row].split(',')]
    L_S = [float(item)/1000 for item in prts[16][row].split(',')]
    L_F = [float(item)/1000 for item in prts[17][row].split(',')]
    L_R = [float(item)/1000 for item in prts[18][row].split(',')]

    K = prts[19][row]

    # Other coefficients
    V_isolant = (sum(L_T)+sum(L_B)+height)*(2*sum(L_S)+width)*(sum(L_F)+sum(L_R)+length) - (L_T[1]+L_B[1]+height)*(2*L_S[1]+width)*\
    (L_F[1]+L_R[1]+length)
    m_isolant = Density*V_isolant/1000
    coef = height*width*(1/L_F[0]+1/L_R[0]) + 2*height*length/L_S[0] + width*length*(1/L_B[0]+1/L_T[0])

    filename = essnum + '.xlsx'
    df = pd.read_excel("data/"+filename,decimal=',',header=None)
    data = df.iloc[7:, 2:26].astype(float)
    # Calculate air density and heat capacity
    # Under standard atmospheric pressure, initial temperature = external temperature
    T_ex = data.iloc[0, 12:24].mean()
    rho = 101325*0.02897/(8.3145*(T_ex+273))
    r = 0.2 # air humidity (in percentage)
    c_a = 1005 # heat capacity of dry air
    c_v = 1996 # heat capacity of water vapour
    c = r*c_v + (1-r)*c_a # heat capacity of air inside 


### ------------------- Display Results--------------------------------------
col1, col2 = st.columns(2)
if prsd:
    with col1:
        ### ------------------- Read Time-Temperature data --------------------------------------
        duration = len(data)
        # st.write(data.iloc[:, 0:12].mean(axis = 1).astype(float))
        plt.plot(list(range(0,duration*2,2)), data.iloc[:, 0:12].mean(axis = 1), label="external temp")
        plt.plot(list(range(0,duration*2,2)), data.iloc[:,12:24].mean(axis = 1), label="internal temp")
        plt.xlabel("time")
        plt.ylabel("temp")
        plt.legend()
        plt.title(essnum)
        # disable the warning
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

    with col2:
        # ---------------------------- Calculate power --------------------------------------
        step = 120 # time interval (seconds)
        # start to calculate from the 2nd minute
        start = 2
        length = 100
        # power = [np.array(cal_puissance(rho,V,m_isolant,c,c_isolant,lamb,length,width,height,coef,step, step_num, data)) for step_num in range(1,length+1)]
        power = [np.array(cal_puissance_n(rho,V,m_isolant,c,c_isolant,K,A,step, step_num, data)) for step_num in range(1,length+1)]
        power_1 = [power[i][0] for i in range(length)]
        power_2 = [power[i][1] for i in range(length)]
        power_t = [power[i][2] for i in range(length)]
        end = 2+2*length
        plt.figure()
        plt.plot(np.arange(start,end,2),power_1,label="Q1")
        plt.plot(np.arange(start,end,2),power_2,label="Q2")
        plt.plot(np.arange(start,end,2),power_t,label="total")
        plt.title(essnum)
        plt.xlabel("time (min)")
        plt.ylabel("refrigerating capacity (W)")
        plt.legend()
        st.pyplot()
