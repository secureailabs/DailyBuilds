import pickle
import sys
from sklearn.model_selection import cross_val_score

mcv = 0
mscore = 0
model = 0
X = 0
y = 0
with open(sys.argv[0], 'rb') as f:
    score = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    cv = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    model = pickle.load(f)
with open(sys.argv[3], 'rb') as f:
    X = pickle.load(f)
with open(sys.argv[4], 'rb') as f:
    y = pickle.load(f)

result = cross_val_score(model, X, y, scoring=mscore, cv=mcv).mean()

with open(sys.argv[5], 'wb') as f:
   pickle.dump(result, f)
