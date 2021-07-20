import pandas as pd
import sys
import pickle

cols = 0
data = 0
with open(sys.argv[0], 'rb') as f:
    cols = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    data = pickle.load(f)

newdf = 0
if data == None:
    newdf = pd.DataFrame(columns = cols)
else:
    newdf = pd.DataFrame(data, columns=cols)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(newdf, f)
