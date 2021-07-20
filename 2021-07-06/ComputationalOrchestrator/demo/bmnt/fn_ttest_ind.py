import pandas as pd
import sys
import pickle
from scipy.stats import ttest_ind

df1 = 0
df2 = 0
with open(sys.argv[0], 'rb') as f:
    df1 = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df2 = pickle.load(f)

ttest_res = ttest_ind(df1, df2)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(ttest_res, f)
