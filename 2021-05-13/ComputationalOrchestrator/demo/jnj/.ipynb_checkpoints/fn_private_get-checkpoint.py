import numpy as np
import pandas as pd
import pickle
import sys

col_id = 0
df = 0

with open(sys.argv[0], 'rb') as f:
    col_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df = pickle.load(f)

df['hash']=df[col_id].apply(hash)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(df['hash'].to_numpy(), f)
