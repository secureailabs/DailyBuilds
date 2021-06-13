import pandas as pd
import sys
import pickle

df = 0
idx = 0
with open(sys.argv[0], 'rb') as f:
    idx = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df = pickle.load(f)

newdf = df.rename(index = idx, inplace=True)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(newdf, f)
