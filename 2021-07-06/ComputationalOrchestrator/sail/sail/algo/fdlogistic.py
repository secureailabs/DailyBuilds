from .fdcore import Algorithm
from ..core import newguid, pushdata, pulldata, pushfn, execjob, registerfn
import torch.nn as nn
import torch

class LogisticRegression(nn.Module):
    def __init__(self, n_input_features):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(n_input_features, 1)
    
    def forward(self,x):
        y_predict = torch.sigmoid(self.linear(x))
        return y_predict

class FdLogistic(Algorithm):
    def __init__(self, vms, vmagg, data, workspace):
        super().__init__(vms, vmagg, data, workspace)
        self.model = 0
        self.parties = 0
        self.fns = self.setfn()
        self.initvms()
    
    def setfn(self):
        fndict = {}
        fndict['logistic_train'] = registerfn("fn_logistic_train.py", 3, 2, 1, 0)[0]
        fndict['logistic_test'] = registerfn("fn_logistic_test.py", 2, 2, 1, 0)[0]
        
        return fndict
    
    def initvms(self):
        for vm in self.vms:
            for key in self.fns:
                pushfn(vm, self.fns[key])
        pushfn(self.vmagg, self.fns['logistic_test'])
    
    def initmodel(self, num_feature):
        m = LogisticRegression(num_feature)
        return m
    
    def train(self, m, num_feature, num_epochs):
        ms = []
        dic = {}
        m_dic = m.state_dict()
        for key in m_dic:
            dic[key] = m_dic[key]
        
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['logistic_train'], [dic, num_feature ,num_epochs], [self.data['X_train'][i], self.data['y_train'][i]], self.workspace)
            execjob(self.vms[i], self.fns['logistic_train'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['logistic_train'], self.workspace)
            ms.append(result[0][0])
        
        sd1 = ms[0].state_dict()
        sd2 = ms[1].state_dict()
        sd3 = {}
        for key in sd1:
            sd3[key] = (sd1[key] + sd2[key]) / 2.

        model3 = LogisticRegression(num_feature)
        model3.load_state_dict(sd3)

        return model3
    
    def test(self, m, num_feature, X_test, y_test):
        dic = {}
        m_dic = m.state_dict()
        for key in m_dic:
            dic[key] = m_dic[key]

        jobid = newguid()
        pushdata(self.vmagg, jobid, self.fns['logistic_test'], [dic, num_feature], [X_test, y_test], self.workspace)
        execjob(self.vmagg, self.fns['logistic_test'], jobid)
        result = pulldata(self.vmagg, jobid, self.fns['logistic_test'], self.workspace)
        acc = result[0][0]
        return float(acc.numpy())