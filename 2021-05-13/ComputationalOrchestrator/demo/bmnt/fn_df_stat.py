import pandas as pd
import sys
import pickle

df = 0
with open(sys.argv[0], 'rb') as f:
    df = pickle.load(f)

stats = df.statistic

with open(sys.argv[1], 'wb') as f:
    pickle.dump(stats, f)
