import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image


st.markdown("<h1 style='text-align: center;'>About</h1>", unsafe_allow_html=True)
st.markdown('<br></br>', unsafe_allow_html=True)
col1, col2 = st.columns([0.4,0.6])
with col1:
    st.markdown('<h4 style="margin-left: 75px;"> Contact </h4>', unsafe_allow_html=True)
    st.markdown('<h6 style="text-align: left;">Tel: (+33) 0640994867</h6>', unsafe_allow_html=True)
    st.markdown('<h6 style="text-align: left;">Email: <a href="mailto:lianghangao98@gmail.com">lianghangao98@gmail.com</a></h6>',unsafe_allow_html=True)
    st.markdown('<h6 style="text-align: left;">Credit: <a href="https://www.cemafroid.fr">https://www.cemafroid.fr</a></h6>',unsafe_allow_html=True)

with col2:
    img = Image.open('cemafroid.jpeg')
    st.image(img)

