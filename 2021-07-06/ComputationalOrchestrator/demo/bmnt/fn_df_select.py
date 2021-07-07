import pandas as pd
import sys
import pickle

df = 0
label = 0
val = 0
with open(sys.argv[0], 'rb') as f:
    label = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    val = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    df = pickle.load(f)

res_df = df[df[label]==val]

with open(sys.argv[3], 'wb') as f:
    pickle.dump(res_df, f)
