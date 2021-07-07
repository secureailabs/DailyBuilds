import pandas as pd
import sys
import pickle

df = 0
adf = 0
with open(sys.argv[0], 'rb') as f:
    df = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    adf = pickle.load(f)

newdf = df.append(adf, ignore_index=True)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(newdf, f)
