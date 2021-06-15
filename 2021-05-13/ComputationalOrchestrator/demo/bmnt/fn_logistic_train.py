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
num_epoch = 0
X_train = 0
y_train = 0
with open(sys.argv[0], 'rb') as f:
    model_dict = pickle.load(f)
with open(sys.argv[1], 'rb') as f:
    num_feature = pickle.load(f)
with open(sys.argv[2], 'rb') as f:
    num_epoch = pickle.load(f)
with open(sys.argv[3], 'rb') as f:
    X_train = pickle.load(f)
with open(sys.argv[4], 'rb') as f:
    y_train = pickle.load(f)

model = LogisticRegression(num_feature)
model.load_state_dict(model_dict)

# Loss and optimizer
# nn.CrossEntropyLoss() computes softmax internally
criterion = nn.BCELoss()  
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  

# Train the model
for epoch in range(num_epoch):
    y_predict = model(X_train)
    y_train = torch.reshape(y_train,(-1,1))
    loss = criterion(y_predict, y_train)
	    
    loss.backward()
	    
    optimizer.step()
	    
    optimizer.zero_grad()
	    
    if(epoch+1)%10==0:
        print(f'epoch:{epoch+1}, loss = {loss.item():.4f}')
	
with open(sys.argv[5], 'wb') as f:
    pickle.dump(model, f)
