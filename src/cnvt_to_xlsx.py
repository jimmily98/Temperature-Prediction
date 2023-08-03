import numpy as np
import pandas as pd
import os
import sys

# Read data from .dat and convert to .xlsx
def cnvtdata(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    print("lines")
    data = []
    for line in lines:
        data.append(line.split(';'))
    df = pd.DataFrame(data)
    df.to_excel(filename[:-4]+'.xlsx', index=False, header=False)


filelist = ['F'+str(i)+'.dat' for i in range(3338, 3347)]
for filename in filelist:
    cnvtdata(filename)
    
