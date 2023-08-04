import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Select data')

@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


col1, col2 = st.columns(2)
with col1:
    st.subheader('Choose your data from the drop-down menu below')
    option = st.selectbox('Select data', ['F3326','F3327','F3328','F3329','F3330','F3331','F3332','F3338', 'F3339', 'F3340', 'F3341', 'F3342', 'F3343', 'F3344', 'F3345', 'F3346'])
    st.session_state['option'] = option
    # read data from .xlsx file
    filename = option + '.xlsx'
    df = pd.read_excel('data/'+filename,decimal=',',header=None)
    deflt = st.checkbox('Use default parameters')


with col2:
    st.subheader('Upload parameters')
    df_sample =pd.read_excel('data/EssaiClient.xlsx',decimal=',',header=None)
    df_sample = convert_df(df_sample)
    st.download_button(
        label="Download sample file",
        data=df_sample,
        file_name='parameters_sample.csv',
        mime='text/csv',
    )
    uploaded_file = col2.file_uploader("Choose a file")

ctm = col1.button('Confirm')
if ctm:
    if deflt:
        df_par = pd.read_excel('data/EssaiClient.xlsx',decimal=',',header=None)
        st.session_state['df_par'] = 1
    else:
        if uploaded_file is not None:
            df_par = pd.read_excel(uploaded_file, decimal=',',header=None)
            st.session_state['df_par'] = 1
        else:
            st.chat_message('Please upload your parameters OR use default parameters')
            st.session_state['df_par'] = 0


### --- draw the data --- ###
# read the data from 3-26 column, from 8th row to the end
data = df.iloc[7:, 2:26]
# draw the data of each column
duration = len(data)
for i in range(24):
    plt.plot(list(range(0,duration*2,2)), data.iloc[:, i].astype(float), label=str(i+1))
plt.xlabel("time")
plt.ylabel("temp")
plt.legend()
plt.title("data_" + filename)
plt.show()
### ------------------- ###


### --- extract information --- ###       
# Client 
# client_list = []
# for num in np.append(np.arange(26,33),np.arange(38,47)):
#     filename = 'F33' + str(num) + '.xlsx'
#     df = pd.read_excel(filename,decimal=',',header=None)
#     client_list.append(df.iloc[2, 2])
# print("Clients: ", np.unique(client_list))
    