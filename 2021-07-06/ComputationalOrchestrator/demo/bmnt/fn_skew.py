import pandas as pd
import sys
import pickle

df = 0
col_id = 0
mean = 0
with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    mean = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    df = pickle.load(f)
    
sumval = 0
col = df[col_id].values
for val in col:
    sumval+=(val - mean)**3

with open(sys.argv[3], 'wb') as f:
    pickle.dump(sumval, f)
