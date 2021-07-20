import pickle
import sys
import pandas as pd

df1 = 0
df2 = 0
inaxis = 0
with open(sys.argv[0], 'rb') as f:
    axis=pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df1=pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    df2=pickle.load(f)

df = pd.concat([df1, df2], axis = inaxis)

with open(sys.argv[3], 'wb') as f:
    pickle.dump(df,f)
