import pickle
import sys
import pandas as pd

df = 0
cols = 0
with open(sys.argv[0], 'rb') as f:
    cols=pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    df=pickle.load(f)

onehot_df = df[cols]
onehot_df = pd.get_dummies(onehot_df, columns = cols)

with open(sys.argv[2], 'wb') as f:
    pickle.dump(onehot_df,f)
