import pandas as pd
import sys
import pickle

df = 0
col_id = 0
with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df = pickle.load(f)

des = df[col_id].describe()

with open(sys.argv[2], 'wb') as f:
    pickle.dump(des, f)
