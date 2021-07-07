import pandas as pd
import sys
import pickle

df = 0
mean = 0
with open(sys.argv[0], 'rb') as f:
    mean = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df = pickle.load(f)

arr = df.to_numpy()
print(mean)
print(df.columns)

s = 0
for i in range(arr.shape[0]):
    s+=(arr[i]-mean)**2
lendf = df.shape[0]

with open(sys.argv[2], 'wb') as f:
    pickle.dump(s, f)
with open(sys.argv[3], 'wb') as f:
    pickle.dump(lendf, f)
