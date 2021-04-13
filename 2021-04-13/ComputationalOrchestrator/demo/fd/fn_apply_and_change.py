import sys
import pickle
import pandas as pd

func = 0
label = 0
data = 0
with open(sys.argv[0], 'rb') as f:
    func = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    label = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    data = pickle.load(f)

for l in label:
    data[l] = data[l].apply(func)
print(data)
print(data.shape)

with open(sys.argv[3], 'wb') as f:
    pickle.dump(data, f)
