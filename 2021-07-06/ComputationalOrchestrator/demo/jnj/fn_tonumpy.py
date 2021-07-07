import sys
import pickle
import pandas as pd

data = 0

with open(sys.argv[0], 'rb') as f:
    data = pickle.load(f)

arr = data.to_numpy()
print(arr)
print(arr.shape)

with open(sys.argv[1], 'wb') as f:
    pickle.dump(arr, f)
