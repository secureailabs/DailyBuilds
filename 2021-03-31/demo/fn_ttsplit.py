import numpy as np
import sys
import pickle
from sklearn.model_selection import train_test_split
import pandas as pd

data = 0
feature = 0
target = 0
testsize = 0

with open(sys.argv[0], 'rb') as f:
    feature = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    target = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    testsize = pickle.load(f)
with open(sys.argv[3], 'rb') as f:
    data = pickle.load(f)

X=data[feature].to_numpy()
y=data[target].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize)

with open(sys.argv[4], 'wb') as f:
    pickle.dump(X_train, f)
with open(sys.argv[5], 'wb') as f:
    pickle.dump(X_test, f)
with open(sys.argv[6], 'wb') as f:
    pickle.dump(y_train, f)
with open(sys.argv[7], 'wb') as f:
    pickle.dump(y_test, f)
