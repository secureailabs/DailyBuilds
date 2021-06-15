import pandas as pd
import sys
import pickle
import torch
import torch.nn as nn
import numpy as np

class LogisticRegression(nn.Module):
    def __init__(self, n_input_features):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(n_input_features, 1)
    
    def forward(self,x):
        y_predict = torch.sigmoid(self.linear(x))
        return y_predict


model_dict = 0
num_feature = 0
X_test = 0
y_test = 0
with open(sys.argv[0], 'rb') as f:
    model_dict = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    num_feature = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    X_test = pickle.load(f)
with open(sys.argv[3], 'rb') as f:
    y_test = pickle.load(f)
    
model = LogisticRegression(num_feature)
model.load_state_dict(model_dict)

acc = 0
with torch.no_grad():
    y_predict = model(X_test)
    y_predict_cls = y_predict.round()
    y_test = torch.reshape(y_test,(-1,1))
    int_arr = y_predict_cls.eq(y_test).long()
    acc = int_arr.sum()/float(y_test.shape[0])
    print(f'accuracy = {acc:.4f}')

with open(sys.argv[4], 'wb') as f:
    pickle.dump(acc, f)
