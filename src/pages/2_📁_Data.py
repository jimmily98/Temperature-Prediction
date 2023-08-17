import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.markdown("<h1 style='text-align: center;'>Select Data</h1>", unsafe_allow_html=True)
st.session_state['df_par'] = 0
st.session_state['option'] = 0

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='text-align: center;'> Choose your data from the drop-down menu below</h3>", unsafe_allow_html=True)
    st.markdown('<br></br>', unsafe_allow_html=True)
    option = st.selectbox('Select data', ['F3326','F3327','F3328','F3329','F3330','F3331','F3332','F3338', 'F3339', 'F3340', 'F3341', 'F3342', 'F3343', 'F3344', 'F3345', 'F3346'])
    st.session_state['option'] = option
    # read data from .xlsx file
    filename = option + '.xlsx'
    df = pd.read_excel('data/'+filename,decimal=',',header=None)
    deflt = st.selectbox('Which parameters do you want to use?', ['Default parameters','Upload parameters'])


with col2:
    st.markdown("<h3 style='text-align: center;'> Upload Parameters</h3>", unsafe_allow_html=True)
    df_sample =pd.read_excel('data/EssaiClient.xlsx',decimal=',',header=None)
    df_sample = convert_df(df_sample)
    st.markdown('<br></br>', unsafe_allow_html=True)
    st.download_button(
        label="Download sample file",
        data=df_sample,
        file_name='parameters_sample.csv',
        mime='text/csv',
    )
    if deflt == 'Upload parameters':
        uploaded_file = col2.file_uploader("Choose a file")
        st.session_state['uploaded_file'] = uploaded_file
        if uploaded_file is not None:
            df_prt = pd.read_excel(uploaded_file,decimal='.',header=None)
            # st.write(df_prt)
            st.write(df_prt.iloc[1:,0])


if deflt == 'Default parameters':
    df_par = pd.read_excel('data/EssaiClient.xlsx',decimal=',',header=None)
    st.session_state['df_par'] = 1
else:
    if uploaded_file is not None:
        df_par = pd.read_excel(uploaded_file, decimal=',',header=None)
        st.session_state['df_par'] = 1
    else:
        st.session_state['df_par'] = 0

    