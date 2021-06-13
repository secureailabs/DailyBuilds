import numpy as np
import sys
import pickle

data = 0
col_id = 0

with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    data = pickle.load(f)

minval = data[col_id].min()

with open(sys.argv[2], 'wb') as f:
    pickle.dump(minval, f)
