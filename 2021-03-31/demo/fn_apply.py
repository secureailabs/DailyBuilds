import pickle
import sys
import pandas as pd

df = 0
func = 0
with open(sys.argv[0], 'rb') as f:
    func=pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df=pickle.load(f)

df = df.apply(func)
print(df)
print(df.shape)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(df,f)
