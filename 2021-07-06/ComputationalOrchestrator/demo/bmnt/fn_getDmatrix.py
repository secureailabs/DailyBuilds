import sys
import pickle
from sklearn.model_selection import train_test_split
import pandas as pd

data = 0
Y_label = 0

with open(sys.argv[0], 'rb') as f:
    data = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    label = pickle.load(f)

D_mat = xgb.DMatrix(data, label=Y_label)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(D_mat, f)
