import pandas as pd
import sys
import pickle
import torch
import torch.nn as nn
import numpy as np

num_feature = 0
with open(sys.argv[0], 'rb') as f:
    num_feature = pickle.load(f)

class LogisticRegression(nn.Module):
    def __init__(self, n_input_features):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(n_input_features, 1)
    
    def forward(self,x):
        y_predict = torch.sigmoid(self.linear(x))
        return y_predict


model = LogisticRegression(num_feature)

with open(sys.argv[1], 'wb') as f:
    pickle.dump(model, f)
