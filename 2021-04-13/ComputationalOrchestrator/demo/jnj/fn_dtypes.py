import sys
import pickle
import pandas as pd

data = 0

with open(sys.argv[0], 'rb') as f:
    data = pickle.load(f)

dtypes = data.dtypes

with open(sys.argv[1], 'wb') as f:
    pickle.dump(dtypes, f)
