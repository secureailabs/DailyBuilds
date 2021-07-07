import sys
import pickle
from sklearn.model_selection import train_test_split
import pandas as pd

X = 0
y = 0

with open(sys.argv[0], 'rb') as f:
    testsize = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    randomstate = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    X = pickle.load(f)
with open(sys.argv[3], 'rb') as f:
    y = pickle.load(f)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=testsize, random_state=randomstate)

with open(sys.argv[4], 'wb') as f:
    pickle.dump(X_train, f)
with open(sys.argv[5], 'wb') as f:
    pickle.dump(X_test, f)
with open(sys.argv[6], 'wb') as f:
    pickle.dump(y_train, f)
with open(sys.argv[7], 'wb') as f:
    pickle.dump(y_test, f)
