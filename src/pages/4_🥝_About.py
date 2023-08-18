import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.markdown("<h1 style='text-align: center;'>About</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.markdown("<h3 style='text-align: center;'> About the project</h3>", unsafe_allow_html=True)
    st.markdown('<br></br>', unsafe_allow_html=True)
    st.markdown('<a href="https://www.cemafroid.fr">https://www.cemafroid.fr</a>', unsafe_allow_html=True)

with col2:
    st.markdown("<h3 style='text-align: center;'> Contact </h3>", unsafe_allow_html=True)
    st.markdown('<br></br>', unsafe_allow_html=True)
    st.markdown('Tel: (+33) 0640994867', unsafe_allow_html=True)
    st.markdown('Email: <a href="mailto:lianghangao98@gmail.com">lianghangao98@gmail.com</a>',unsafe_allow_html=True)
