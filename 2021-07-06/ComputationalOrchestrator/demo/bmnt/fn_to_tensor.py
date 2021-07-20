import pandas as pd
import sys
import pickle
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler

arr = 0
tran_bit = 0
with open(sys.argv[0], 'rb') as f:
    tran_bit = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    arr = pickle.load(f)

if(tran_bit == 1):
    sc = StandardScaler()
    arr = sc.fit_transform(arr)
 
tensor_arr = torch.from_numpy(arr.astype(np.float32))

with open(sys.argv[2], 'wb') as f:
    pickle.dump(tensor_arr, f)
