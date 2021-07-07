import pandas as pd
import sys
import pickle

df = 0
with open(sys.argv[0], 'rb') as f:
    df = pickle.load(f)

sample =df.head(5)

with open(sys.argv[1], 'wb') as f:
    pickle.dump(sample, f)
