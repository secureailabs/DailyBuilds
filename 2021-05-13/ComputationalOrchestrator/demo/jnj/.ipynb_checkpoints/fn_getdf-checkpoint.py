import pandas as pd
import sys
import pickle
from io import StringIO
import _DataConnector as dc

with open(sys.argv[0], 'rb') as f:
    tableID = pickle.load(f)

buffer = dc.ReadBuffer(tableID)
df = pd.read_csv(StringIO(buffer))

shape = df.shape
col_label = df.columns

with open(sys.argv[1], 'wb') as f:
    pickle.dump(shape, f)
with open(sys.argv[2], 'wb') as f:
    pickle.dump(col_label, f)
with open(sys.argv[3], 'wb') as f:
    pickle.dump(df, f)
