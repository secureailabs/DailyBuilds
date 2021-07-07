import pandas as pd
import sys
import pickle

df =0
with open(sys.argv[0], 'rb') as f:
    df = pickle.load(f)

num = df.shape[1]

with open(sys.argv[1], 'wb') as f:
    pickle.dump(num, f)
