import pickle
import sys
import pandas as pd

df = 0
mtype = 0
with open(sys.argv[0], 'rb') as f:
    mtype=pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df=pickle.load(f)

df = df.astype(mtype)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(df,f)
