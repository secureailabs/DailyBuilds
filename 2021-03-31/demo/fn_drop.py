import pickle
import sys
import pandas as pd

df = 0
col = 0
inaxis = 0
with open(sys.argv[0], 'rb') as f:
    col=pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    inaxis=pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    df=pickle.load(f)

df_drop = df.drop(col, axis = inaxis)

with open(sys.argv[3], 'wb') as f:
    pickle.dump(df_drop,f)
