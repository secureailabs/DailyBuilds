import numpy as np
import pickle
import sys
import pandas as pd

col_id = 0
data = 0
with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    data = pickle.load(f)
    
mean = data[col_id].mean()

with open(sys.argv[2], 'wb') as f:
    pickle.dump(mean, f)
