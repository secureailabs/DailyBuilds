import numpy as np
import sys
import pickle

data = 0
col_id = 0

with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    data = pickle.load(f)

maxval = data[col_id].max()

with open(sys.argv[2], 'wb') as f:
    pickle.dump(maxval, f)
