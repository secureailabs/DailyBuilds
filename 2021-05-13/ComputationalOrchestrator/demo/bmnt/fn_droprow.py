import pandas as pd
import sys
import pickle

df =0
label = 0

with open(sys.argv[0], 'rb') as f:
    label=pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df=pickle.load(f)

df = df.drop(index = label)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(df,f)
