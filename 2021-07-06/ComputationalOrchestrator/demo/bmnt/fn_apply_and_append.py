import sys
import pickle
import pandas as pd

label = 0
newlabel = 0
data = 0
with open(sys.argv[0], 'rb') as f:
    label = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    newlabel = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    data = pickle.load(f)

data[newlabel] = (data[label]-32)*5/9
print(data)
print(data.shape)

with open(sys.argv[3], 'wb') as f:
    pickle.dump(data, f)
