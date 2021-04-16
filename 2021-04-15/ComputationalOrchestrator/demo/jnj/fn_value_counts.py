import pickle
import sys
import pandas as pd

df = 0
col = 0
with open(sys.argv[0], 'rb') as f:
    col=pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df=pickle.load(f)

df_vc = df[col].value_counts()

with open(sys.argv[2], 'wb') as f:
    pickle.dump(df_vc,f)
