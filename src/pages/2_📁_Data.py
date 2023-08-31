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

# Git repo
repo_url = 'https://github.com/jimmily98/Temperature-Prediction'


# Page Title & states
st.markdown("<h1 style='text-align: center;'>Select Data</h1>", unsafe_allow_html=True)
st.session_state['df_par'] = 0
st.session_state['option'] = 0
st.session_state['df_options'] = []

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')

cont1 = st.container()
with cont1:
    col1, col2 = st.columns(2)
    with col1:
        # st.markdown("<h3 style='text-align: center;'> Choose your data from the drop-down menu below</h3>", unsafe_allow_html=True)
        st.markdown('<br></br>', unsafe_allow_html=True)
        deflt = st.selectbox('Choose parameters', ['Default parameters','Upload parameters'])
        if deflt == "Default parameters":
            st.session_state['df_options'] = ['F3326','F3327','F3328','F3329','F3330','F3331','F3332','F3338', 'F3339', 'F3340', 'F3341', 'F3342', 'F3343', 'F3344', 'F3345', 'F3346']


    with col2:
        # st.markdown("<h3 style='text-align: center;'> Upload Parameters</h3>", unsafe_allow_html=True)
        uploaded_data = col2.file_uploader("Upload New Data")
        df_data =pd.read_excel('data/F3326.xlsx',decimal=',',header=None)
        df_data = convert_df(df_data)
        st.download_button(
            label="Download sample data",
            data=df_data,
            file_name='F3326.csv',
            mime='text/csv',
        )
        if deflt == 'Upload parameters':
            uploaded_file = col2.file_uploader("Choose a file")
            st.session_state['uploaded_file'] = uploaded_file

            df_sample =pd.read_excel('data/EssaiClient.xlsx',decimal=',',header=None)
            df_sample = convert_df(df_sample)
            st.markdown('<br></br>', unsafe_allow_html=True)
            st.download_button(
                label="Download sample file",
                data=df_sample,
                file_name='parameters_sample.csv',
                mime='text/csv',
            )
            if uploaded_file is not None:
                df_prt = pd.read_excel(uploaded_file,decimal='.',header=None)
                st.write(df_prt.iloc[1:,0])
                st.session_state['df_options'] = df_prt.iloc[1:,0]

    option = col1.selectbox('Select data', options = st.session_state['df_options'])
    st.session_state['option'] = option
    # read data from .xlsx file

    if option != None:
        filename = option + '.xlsx'
        df = pd.read_excel('data/'+filename,decimal=',',header=None)

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