import pandas as pd
import sys
import pickle

df = 0
with open(sys.argv[0], 'rb') as f:
    df = pickle.load(f)

meandf = df.mean()
lendf = df.shape[0]

with open(sys.argv[1], 'wb') as f:
    pickle.dump(meandf, f)
with open(sys.argv[2], 'wb') as f:
    pickle.dump(lendf, f)
