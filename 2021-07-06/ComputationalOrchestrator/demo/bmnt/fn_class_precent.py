import pandas as pd
import sys
import pickle

df = 0
label1 = 0
label2 = 0
with open(sys.argv[0], 'rb') as f:
    label1 = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    label2 = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    df = pickle.load(f)

denominator = len(df[df[label1] == label2].index) 
numerator = len(df[df[label1] == label2].index) + len(df[df[label1] != label2].index)

with open(sys.argv[3], 'wb') as f:
    pickle.dump(denominator, f)
with open(sys.argv[4], 'wb') as f:
    pickle.dump(numerator, f)
