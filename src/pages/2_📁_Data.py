import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from st_btn_select import st_btn_select
import git
import os
import streamlit_extras
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.row import row


# Page Title & states
st.markdown("<h1 style='text-align: center;'>Data and Parameters</h1>", unsafe_allow_html=True)
# "df_par" == 0: parameters not uploaded; "df_par" == 1: parameters uploaded
st.session_state['df_par'] = 0

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


cont1 = st.container()
with cont1:
    row1 = row([2, 4, 1], vertical_align="center")
    deflt = row1.selectbox('Choose parameters', ['Default parameters','Upload parameters'])
    if deflt == "Default parameters":
        st.session_state['df_options'] = ['F3326','F3327','F3328','F3329','F3330','F3331','F3332','F3338', 'F3339', 'F3340', 'F3341', 'F3342', 'F3343', 'F3344', 'F3345', 'F3346']
    if deflt == "Upload parameters" and st.session_state['updated_file'] == 0:
        st.session_state['df_options'] = []

    uploaded_data = row1.file_uploader("Upload New Data")
    df_data =pd.read_excel('data/F3326.xlsx',decimal=',',header=None)
    df_data = convert_df(df_data)
    row1.download_button(
        label="Sample",
        data=df_data,
        file_name='F3326.csv',
        mime='text/csv',
    )

    row2 = row([2, 4, 1], vertical_align="center")

    option = row2.selectbox('Select data', options = st.session_state['df_options'])
    # read data from .xlsx file
    if option != None:
        filename = option + '.xlsx'
        df = pd.read_excel('data/'+filename,decimal=',',header=None)
    
    # With Uploaded parameters
    uploaded_file = row2.file_uploader("Upload parameters")

    df_sample =pd.read_excel('data/EssaiClient.xlsx',decimal=',',header=None)
    df_sample = convert_df(df_sample)
    st.markdown('<br></br>', unsafe_allow_html=True)
    row2.download_button(
        label="Sample",
        data=df_sample,
        file_name='parameters_sample.csv',
        mime='text/csv',
    )
    
    # Only data in parameters file are available
    if uploaded_file is None:
        st.session_state['updated_file'] = 0
    if deflt == 'Upload parameters' and uploaded_file is None:
        st.session_state['have_rerun'] = 0
    if deflt == 'Upload parameters' and uploaded_file is not None:
        df_prt = pd.read_excel(uploaded_file,decimal='.',header=None)
        st.session_state['df_options'] = df_prt.iloc[1:,0]
        st.session_state['updated_file'] = 1
        if st.session_state['have_rerun'] == 0:
            st.session_state['have_rerun'] = 1
            st.experimental_rerun()

    # Read parameters
    if deflt == 'Default parameters':
        df_par = pd.read_excel('data/EssaiClient.xlsx',decimal=',',header=None)
        st.session_state['df_par'] = 1
    else:
        if uploaded_file is not None:
            df_par = pd.read_excel(uploaded_file, decimal=',',header=None)
            st.session_state['df_par'] = 1
        else:
            st.session_state['df_par'] = 0

if_ready = st.button("Go to Display page to see results")
if if_ready:
    switch_page("Display")
