import numpy as np
import pandas as pd
import pickle
import sys

x_id = 0
y_id = 0
xmean = 0
ymean = 0
xdf = 0
ydf = 0

with open(sys.argv[0], 'rb') as f:
    x_id = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    y_id = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    xmean = pickle.load(f)
with open(sys.argv[3], 'rb') as f:
    ymean = pickle.load(f)
with open(sys.argv[4], 'rb') as f:
    df = pickle.load(f)
    
xval = df[x_id].values
yval = df[y_id].values

sumprod = 0
sumsx = 0
sumsy = 0

for i in range(len(xval)):
    sumprod += (xval[i]-xmean)*(yval[i]-ymean)
    sumsx += (xval[i]-xmean)**2
    sumsy += (yval[i]-ymean)**2

with open(sys.argv[5], 'wb') as f:
    pickle.dump(sumprod, f)
with open(sys.argv[6], 'wb') as f:
    pickle.dump(sumsx, f)
with open(sys.argv[7], 'wb') as f:
    pickle.dump(sumsy, f)

