import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title('Select data')

col1, col2 = st.columns(2)
with col1:
    st.subheader('Choose your data from the drop-down menu below')
    option = st.selectbox('Select data', ['F3338', 'F3339', 'F3340', 'F3341', 'F3342', 'F3343', 'F3344', 'F3345', 'F3346'])
    # read data from .xlsx file
    filename = option + '.xlsx'
    df = pd.read_excel('data/'+filename,decimal=',',header=None)

with col2:
    st.subheader('Upload parameters')
    df_sample =pd.read_excel('data/EssaiClient.xlsx',decimal=',',header=None)
    df_sample.to_csv().encode('utf-8')
    st.download_button(
    label="Download sample file",
    data=df_sample,
    file_name='parameters_sample.csv',
    )
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df_par = pd.read_excel(uploaded_file,decimal=',',header=None)


# read data from .xlsx file
filename = option + '.xlsx'
df = pd.read_excel('data/'+filename,decimal=',',header=None)

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
    