from ..core import connect, newguid, pushdata, pulldata, pushfn, execjob, registerfn
import numpy as np
from scipy.stats import t

class DataFrameGroup:
    def __init__(self, vms, workplace):
        self.vms = vms
        self.workspace = workplace
        self.col_label = []
        self.shape = []
        self.df = []
        self.fns = self.setfn()
        self.initvms()
    
    def setfn(self):
        fndict = {}
        fndict['import'] = registerfn("fn_getdf.py", 1, 0, 2, 1)[0]
        fndict['sample'] = registerfn("fn_sample.py", 0, 1, 1, 0)[0]
        fndict['col_des'] = registerfn("col_describe.py", 1, 1, 1, 0)[0]
        fndict['std_trans'] = registerfn("stand_fd.py", 3, 1, 0, 1)[0]
        fndict['norm_trans'] = registerfn("normal_fd.py", 3, 1, 0, 1)[0]
        fndict['log_trans'] = registerfn("fn_logtrans.py", 2, 1, 0, 1)[0]
        fndict['mean'] = registerfn("fn_fd_mean.py", 1, 1, 1, 0)[0]
        fndict['std'] = registerfn("fn_fd_sdeviation.py", 2, 1, 1, 0)[0]
        fndict['min'] = registerfn("fn_fd_min.py", 1, 1, 1, 0)[0]
        fndict['max'] = registerfn("fn_fd_max.py", 1, 1, 1, 0)[0]
        fndict['skew'] = registerfn("fn_skew.py", 2, 1, 1, 0)[0]
        fndict['train_test'] = registerfn("fn_train_test_split.py", 2, 2, 0, 4)[0]
        fndict['get_col'] = registerfn("fn_getcol.py", 1, 1, 0, 1)[0]
        fndict['onehot'] = registerfn("fn_onehot.py", 1, 1, 0, 1)[0]
        fndict['concat'] = registerfn("fn_concat.py", 1, 2, 0, 1)[0]
        fndict['drop'] = registerfn("fn_drop.py", 2, 1, 0, 1)[0]
        fndict['astype']=registerfn("fn_astype.py", 1, 1, 0, 1)[0]
        fndict['apply']=registerfn("fn_apply.py", 1, 1, 0, 1)[0]
        fndict['apply_and_change'] = registerfn("fn_apply_and_change.py", 2, 1, 0, 1)[0]
        fndict['apply_and_append'] = registerfn("fn_apply_and_append.py", 2, 1, 0, 1)[0]
        fndict['value_counts'] = registerfn("fn_value_counts.py", 1, 1, 1, 0)[0]
        fndict['get_Dmat'] = registerfn("fn_getDmatrix.py", 0, 2, 0, 1)[0]
        fndict['dtypes'] = registerfn("fn_dtypes.py", 0, 1, 1, 0)[0]
        fndict['to_numpy'] = registerfn("fn_tonumpy.py", 0, 1, 0, 1)[0]
        fndict['private_get'] = registerfn("fn_private_get.py", 1, 1, 1, 0)[0]
        fndict['droprow'] = registerfn("fn_droprow.py", 1, 1, 0, 1)[0]
        fndict['pearson'] = registerfn("fn_pearson.py", 4, 1, 3, 0)[0]
        fndict['df_mean'] = registerfn("fn_df_mean.py", 0, 1, 2, 0)[0]
        fndict['df_std'] = registerfn("fn_df_std.py", 1, 1, 2, 0)[0]
        fndict['class_precent'] = registerfn("fn_class_precent.py", 2, 1, 2, 0)[0]
        fndict['df_select'] = registerfn("fn_df_select.py", 2, 1, 0, 1)[0]
        fndict['df_size'] = registerfn("fn_df_size.py", 0, 1, 1, 0)[0]
        fndict['df_col'] = registerfn("fn_df_col.py", 0, 1, 1, 0)[0]
        fndict['df_gen_df'] = registerfn("fn_gen_df.py", 0, 2, 1, 0)[0]
        fndict['bin_cate'] = registerfn("fn_bin_cate.py", 1, 1, 0, 1)[0]
        fndict['to_tensor'] = registerfn("fn_to_tensor.py", 1, 1, 0, 1)[0]
        fndict['feature_num'] = registerfn("fn_feature_num.py", 0, 1, 1, 0)[0]
        return fndict

    def initvms(self):
        for vm in self.vms:
            for key in self.fns:
                pushfn(vm, self.fns[key])
    
    def import_data(self, data_id):
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['import'], [data_id[i]], [], self.workspace)
            execjob(self.vms[i], self.fns['import'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['import'], self.workspace)
            self.shape.append(result[0][0])
            self.col_label.append(result[0][1])
            self.df.append(result[1][0])

    def sample(self, vm, data):
        jobid = newguid()
        pushdata(vm, jobid, self.fns['sample'], [], [data], self.workspace)
        execjob(vm, self.fns['sample'], jobid)
        result = pulldata(vm, jobid, self.fns['sample'], self.workspace)
        return result[0][0]
    
    def dtypes(self):
        dtypes = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['dtypes'], [], [self.df[i]], self.workspace)
            execjob(self.vms[i], self.fns['dtypes'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['dtypes'], self.workspace)
            dtypes.append(result[0][0])
        return dtypes
    
    def col_describe(self, vm, data, col_id):
        jobid = newguid()
        pushdata(vm, jobid, self.fns['col_des'], [col_id], [data], self.workspace)
        execjob(vm, self.fns['col_des'], jobid)
        result = pulldata(vm, jobid, self.fns['col_des'], self.workspace)
        return result[0][0]

    def log_transform(self, col_id, newcol_id):
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['log_trans'], [col_id, newcol_id], [self.df[i]], self.workspace)
            execjob(self.vms[i], self.fns['log_trans'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['log_trans'], self.workspace)
            self.df[i] = result[1][0]
   
    def std_transform(self, col_id, mean, stdev):
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['std_trans'], [col_id, mean, stdev], [self.df[i]], self.workspace)
            execjob(self.vms[i], self.fns['std_trans'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['std_trans'], self.workspace)
            
    def norm_transform(self, col_id, df):
        minval, maxval = self.limit(col_id, df)
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['norm_trans'], [col_id, minval, maxval], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['norm_trans'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['norm_trans'], self.workspace)
                
    def mean(self, col_id, df):
        meanlist = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['mean'], [col_id], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['mean'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['mean'], self.workspace)
            meanlist.append(result[0][0])
        
        sumval = 0
        sumelement = 0
        for i in range(len(self.vms)):
            sumval += meanlist[i]*self.shape[i][0]
            sumelement += self.shape[i][0]
        mean = sumval/sumelement
        
        return mean
    
    def standard_deviation(self, col_id, mean, df):
        sumdevlist = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['std'], [col_id, mean], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['std'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['std'], self.workspace)
            sumdevlist.append(result[0][0])
        sumdev = 0
        sumelement = 0
        for i in range(len(self.vms)):
            sumdev += sumdevlist[i]
            sumelement += self.shape[i][0]
        stddev = (sumdev/sumelement)**0.5
        return stddev
    
    def limit(self, col_id, df):
        minlist = []
        maxlist = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['min'], [col_id], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['min'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['min'], self.workspace)
            minlist.append(result[0][0])
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['max'], [col_id], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['max'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['max'], self.workspace)
            maxlist.append(result[0][0])
        minval = min(minlist)
        maxval = max(maxlist)
        
        return minval, maxval

    def skew(self, col_id, mean, std):
        sumskewlist = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['skew'], [col_id, mean], [self.df[i]], self.workspace)
            execjob(self.vms[i], self.fns['skew'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['skew'], self.workspace)
            sumskewlist.append(result[0][0])
        N = sum(i for i, _ in self.shape)
        skew = (N*(N-1))**0.5*sum(sumskewlist)/N/(N-2)/(std**3)
        return skew
    
    def train_test_split(self, X, y, testsize, randomstate):
        X_train = []
        X_test = []
        y_train = []
        y_test = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['train_test'], [testsize, randomstate], [X[i], y[i]], self.workspace)
            execjob(self.vms[i], self.fns['train_test'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['train_test'], self.workspace)
            X_train.append(result[1][0])
            X_test.append(result[1][1])
            y_train.append(result[1][2])
            y_test.append(result[1][3])
        return X_train, X_test, y_train, y_test
    
    def get_col(self, label, df):
        cols = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['get_col'], [label[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['get_col'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['get_col'], self.workspace)
            cols.append(result[1][0])
        return cols
    
    def onehot(self, label, df):
        dfs = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['onehot'], [label[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['onehot'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['onehot'], self.workspace)
            dfs.append(result[1][0])
        return dfs
    
    def concat(self, df1, df2, axis):
        dfs = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['concat'], [axis], [df1[i], df2[i]], self.workspace)
            execjob(self.vms[i], self.fns['concat'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['concat'], self.workspace)
            dfs.append(result[1][0])
        return dfs
    
    def drop(self, label, axis, df):
        dfs = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['drop'], [label[i], axis[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['drop'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['drop'], self.workspace)
            dfs.append(result[1][0])
        return dfs
    
    def droprow(self, vm, index, df):
        jobid = newguid()
        pushdata(vm, jobid, self.fns['droprow'], [index], [df], self.workspace)
        execjob(vm, self.fns['droprow'], jobid)
        result = pulldata(vm, jobid, self.fns['droprow'], self.workspace)
        df = result[1][0]
        return df

    def astype(self, mtype, df):
        dfs = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['astype'], [mtype[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['astype'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['astype'], self.workspace)
            dfs.append(result[1][0])
        return dfs

    def apply(self, func, df):
        dfs = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['apply'], [func[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['apply'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['apply'], self.workspace)
            dfs.append(result[1][0])
        return dfs
    
    def apply_and_change(self, func, label, df):
        dfs = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['apply_and_change'], [func[i], label[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['apply_and_change'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['apply_and_change'], self.workspace)
            dfs.append(result[1][0])
        return dfs

    def apply_and_append(self, label, newlabel, df):
        dfs = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['apply_and_append'], [label[i], newlabel[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['apply_and_append'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['apply_and_append'], self.workspace)
            dfs.append(result[1][0])
        return dfs

    def value_counts(self, label, df):
        dfs = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['value_counts'], [label[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['value_counts'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['value_counts'], self.workspace)
            dfs.append(result[0][0])
        return dfs

    def to_Dmatrix(self, X, y):
        Dmats = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['get_Dmat'], [], [X[i], y[i]], self.workspace)
            execjob(self.vms[i], self.fns['get_Dmat'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['get_Dmat'], self.workspace)
            Dmats.append(result[1][0])
        return Dmats
    
    def to_numpy(self, df):
        arr = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['to_numpy'], [], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['to_numpy'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['to_numpy'], self.workspace)
            arr.append(result[1][0])
        return arr
    
    def private_intersect(self, vmid1, vmid2, df1, df2, col_id):
        x=0
        y=0

        jobid = newguid()
        pushdata(vmid1, jobid, self.fns['private_get'], [col_id], [df1], self.workspace)
        execjob(vmid1, self.fns['private_get'], jobid)
        result = pulldata(vmid1, jobid, self.fns['private_get'], self.workspace)
        x=result[0][0]

        jobid = newguid()
        pushdata(vmid2, jobid, self.fns['private_get'], [col_id], [df2], self.workspace)
        execjob(vmid2, self.fns['private_get'], jobid)
        result = pulldata(vmid2, jobid, self.fns['private_get'], self.workspace)
        y=result[0][0]

        result1 = np.where(np.in1d(x, y))[0]
        result2 = np.where(np.in1d(y, x))[0]
        return [result1, result2]

    def pearson_corr(self, xlabel, ylabel, df):
        xmean = self.mean(xlabel, df)
        ymean = self.mean(ylabel, df)

        sumprod = 0
        sumsx = 0
        sumsy = 0
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['pearson'], [xlabel, ylabel, xmean, ymean], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['pearson'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['pearson'], self.workspace)
            sumprod+=result[0][0]
            sumsx += result[0][1]
            sumsy += result[0][2]
        return sumprod/((sumsx*sumsy)**0.5)
    
    def df_mean(self, df):
        s = 0
        num = 0
        mean_arr = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['df_mean'], [], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['df_mean'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['df_mean'], self.workspace)
            s += result[0][0]*result[0][1]
            num += result[0][1]
            mean_arr.append(result[0][0])
        mean_arr.append(s/num)
        return mean_arr
    
    def df_std(self, df_mean, df):
        s = 0
        num = 0
        std_arr = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['df_std'], [df_mean], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['df_std'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['df_std'], self.workspace)
            s += result[0][0]
            num += result[0][1]
            std_arr.append((result[0][0]/result[0][1])**0.5)
        std_arr.append((s/num)**0.5)
        return std_arr
    
    def df_var(self, df):
        s = 0
        num = 0
        dfmean = self.df_mean(df)[-1]
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['df_std'], [dfmean], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['df_std'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['df_std'], self.workspace)
            s += result[0][0]
            num += result[0][1]
        return s/(num-1)

    def df_size(self, df):
        sz = 0
        sz_arr = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['df_size'], [], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['df_size'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['df_size'], self.workspace)
            sz += result[0][0]
            sz_arr.append(result[0][0])
        sz_arr.append(sz)
        return sz_arr
    
    def ttest_ind_mono(self, df1, df2):
        mu1 = self.df_mean(df1)
        mu2 = self.df_mean(df2)
        s1 = self.df_std(mu1[-1], df1)
        s2 = self.df_std(mu2[-1], df2)
        n1 = self.df_size(df1)
        n2 = self.df_size(df2)

        t_res = []
        for i in range(len(self.vms)):
            t_tmp = (mu1[i]-mu2[i])/(((n1[i]-1)*s1[i]**2+(n2[i]-1)*s2[i]**2)*(1/n1[i]+1/n2[i])/(n1[i]+n2[i]-2))**0.5
            t_tmp_pvalue = t.sf(t_tmp.abs(), n1[i]+n2[i]-2)
            t_tmp_stat = t_tmp.to_numpy()
            t_res.append([t_tmp_pvalue, t_tmp_stat])
        return t_res

    def ttest_ind(self, df1, df2):
        mu1 = self.df_mean(df1)[-1]
        mu2 = self.df_mean(df2)[-1]
        s1 = self.df_std(mu1, df1)[-1]
        s2 = self.df_std(mu2, df2)[-1]
        n1 = self.df_size(df1)[-1]
        n2 = self.df_size(df2)[-1]

        t_res = (mu1-mu2)/(((n1-1)*s1**2+(n2-1)*s2**2)*(1/n1+1/n2)/(n1+n2-2))**0.5
        pvalue = t.sf(t_res.abs(), n1+n2-2)
        statistics = t_res.to_numpy()

        return statistics, pvalue

    def ttest_ind_mutual(self, df):
        mean_arr = []
        num_arr = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['df_mean'], [], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['df_mean'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['df_mean'], self.workspace)
            mean_arr.append(result[0][0])
            num_arr.append(result[0][1])
        
        std_arr = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['df_std'], [mean_arr[i]], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['df_std'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['df_std'], self.workspace)
            std_arr.append((result[0][0]/result[0][1])**0.5)
        
        ttest_arr=[]
        lenarr=len(self.vms)
        for i in range(lenarr):
            t_res = (mean_arr[i]-mean_arr[(i+1)%lenarr])/(((num_arr[i]-1)*std_arr[i]**2+(num_arr[(i+1)%lenarr]-1)*std_arr[(i+1)%lenarr]**2)*(1/num_arr[i]+1/num_arr[(i+1)%lenarr])/(num_arr[i]+num_arr[(i+1)%lenarr]-2))**0.5
            ttest_arr.append(t_res)
        
        return ttest_arr
    
    def label_precentage(self, label1, label2, df):
        sumde = 0
        sumnu = 0
        pre_res = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['class_precent'], [label1, label2], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['class_precent'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['class_precent'], self.workspace)
            sumde += result[0][0]
            sumnu += result[0][1]
            pre_res.append(result[0][0]/result[0][1])
        pre_res.append(sumde/sumnu)
        return pre_res

    def df_select(self, label, val, df):
        res_df = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['df_select'], [label, val], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['df_select'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['df_select'], self.workspace)
            res_df.append(result[1][0])
        return res_df
    
    def df_col_name(self, df):
        col_name = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['df_col'], [], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['df_col'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['df_col'], self.workspace)
            col_name.append(result[0][0])
        return col_name
    
    def df_get_feature_num(self, df):
        jobid = newguid()
        pushdata(self.vms[0], jobid, self.fns['feature_num'], [], [df], self.workspace)
        execjob(self.vms[0], self.fns['feature_num'], jobid)
        result = pulldata(self.vms[0], jobid, self.fns['feature_num'], self.workspace)
        return result[0][0]
    
    # def gen_df(self, col, data):
    #     df = []
    #     for i in range(len(self.vms)):
    #         jobid = newguid()
    #         pushdata(self.vms[i], jobid, self.fns['df_gen_df'], [col[i], data[i]], [], self.workspace)
    #         execjob(self.vms[i], self.fns['df_gen_df'], jobid)
    #         result = pulldata(self.vms[i], jobid, self.fns['df_gen_df'], self.workspace)
    #         df.append(result[0][0])
    #     return df
    def bin_cate(self, df, col_name):
        new_df = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['bin_cate'], [col_name], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['bin_cate'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['bin_cate'], self.workspace)
            new_df.append(result[1][0])
        return new_df

    def to_tensor(self, df, trans_bit):
        tensors = []
        for i in range(len(self.vms)):
            jobid = newguid()
            pushdata(self.vms[i], jobid, self.fns['to_tensor'], [trans_bit], [df[i]], self.workspace)
            execjob(self.vms[i], self.fns['to_tensor'], jobid)
            result = pulldata(self.vms[i], jobid, self.fns['to_tensor'], self.workspace)
            tensors.append(result[1][0])
        return tensors
