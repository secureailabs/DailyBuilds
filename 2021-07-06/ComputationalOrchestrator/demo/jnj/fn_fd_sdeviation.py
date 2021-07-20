import numpy as np
import pickle
import sys
import pandas as pd

data = 0
col_id = 0
mean = 0
with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    mean = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    data = pickle.load(f)

col = data[col_id].values
sumdev = 0
for x in col:
    sumdev += (x-mean)**2

with open(sys.argv[3], 'wb') as f:
    pickle.dump(sumdev, f)
