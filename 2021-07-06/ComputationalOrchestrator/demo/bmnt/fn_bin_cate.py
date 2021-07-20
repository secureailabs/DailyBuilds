import pandas as pd
import sys
import pickle

df = 0
col_name = 0
with open(sys.argv[0], 'rb') as f:
    col_name = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df = pickle.load(f)

diag_cate={'B':0, 'M':1}
df[col_name] = df[col_name].apply(lambda x: diag_cate[x])

with open(sys.argv[2], 'wb') as f:
    pickle.dump(df, f)
