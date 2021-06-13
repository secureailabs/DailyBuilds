import numpy as np
import pandas as pd
import pickle
import sys
import hashlib

col_id = 0
df = 0

with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df = pickle.load(f)

col = df[col_id].values
hashval = []
for val in col:
    hashval.append(hashlib.sha224(val.encode('ASCII')).hexdigest())

with open(sys.argv[2], 'wb') as f:
    pickle.dump(hashval, f)
