import numpy as np
import sys
import pickle

data = np.random.normal(1, 3, size=(20,20))

print(data)
print(sys.argv[0])

with open(sys.argv[0], 'wb') as f:
    pickle.dump(data, f)
