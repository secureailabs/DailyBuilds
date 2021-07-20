import sys
import pickle
import numpy as np 
import pandas as pd

data = 0
col_id = 0
newcol_id = 0
with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    newcol_id = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    data = pickle.load(f)
    
data[newcol_id] = np.log(data[col_id])

with open(sys.argv[3], 'wb') as f:
    pickle.dump(data, f)
