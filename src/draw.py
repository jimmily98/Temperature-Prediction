import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data from .xlsx file
filename = 'F3330.xlsx'
df = pd.read_excel(filename,decimal=',',header=None)

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
    