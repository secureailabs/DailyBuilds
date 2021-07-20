import pandas as pd
import sys
import pickle

df = 0
dimx = 0
dimy = 0
with open(sys.argv[0], 'rb') as f:
    dimx = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    dimy = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    df = pickle.load(f)

newdf = df.reshape(dimx, dimy)

with open(sys.argv[3], 'wb') as f:
    pickle.dump(newdf, f)
