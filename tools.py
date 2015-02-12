import numpy as np
import pickle
import time
class pca_norm(object):
    def __init__(self, arr, k=1):
        self.k=k
        self.arr = arr

    def norm(self):
        self.u, self.s, self.v = np.linalg.svd(self.arr, full_matrices=True)
        self.arr_k_proj= np.dot(self.u[:,:self.k], np.diag(self.s)[:self.k,:self.k])
        self.norm_obj = Norm_ism(self.arr_k_proj)
        self.arr_k_proj_norm = self.norm_obj.norm()
        self.exp_var = np.cumsum(self.s**2) / np.sum(self.s**2)
        return self.arr_k_proj_norm

    def unnorm(self, arr):
        return np.dot(self.norm_obj.unnorm(arr), self.v[:self.k,:])


class Norm_ism(object):
    def __init__(self, arr):
        self.arr = arr
        self.min =  np.min(self.arr.flatten())
        arr_norm = (self.arr - self.min)
        self.max = np.max(arr_norm.flatten());
        return None

    def norm(self):
            self.arr_norm = ((self.arr - self.min) / self.max)-0.5
            return self.arr_norm 
    
    def unnorm(self, arr=[]):
        if(len(arr)==0):
            arr = self.arr_norm
            self.arr = (arr * self.max) + self.min
        else:
            return ((arr+.5) * self.max) + self.min

def parse_file(file_name):
    with open(file_name, 'r') as f:
        read_data = f.read()
    f.closed
    out = []
    labels = []
    file_lines = read_data.split('\n')
    for row in range(len(file_lines)):
        if row >= 1:
            out_temp = [[]]
            col_data = file_lines[row].split(',')
            if len(col_data)>=2:
                repeat = len(col_data[1].split(' '))
                out_temp = [x[:] for x in [[None] * 25] * (repeat)]
                id_n = float(col_data[0])
                exp_rain = float(col_data[len(col_data) - 1])
                for col in range(len(col_data) + 5):
                    for i in range(repeat):
                        if col == 0:
                            out_temp[i][col] = id_n
                        elif col == (len(col_data) + 5 - 1):
                            out_temp[i][col] = exp_rain
                        elif col == (len(col_data) + 5- 2):
                            if '-99000' in file_lines[row]:
                                out_temp[i][col] = 1.0
                            else:
                                out_temp[i][col] = 0.0
                        elif col == (len(col_data)+ 5 - 3):
                            if '-99001' in file_lines[row]:
                                out_temp[i][col] = 1.0
                            else:
                                out_temp[i][col] = 0.0
                        elif col == (len(col_data)+ 5 - 4):
                            if '-99003' in file_lines[row]:
                                out_temp[i][col] = 1.0
                            else:
                                out_temp[i][col] = 0.0
                        elif col == (len(col_data)+ 5 - 5):
                            if 'nan' in file_lines[row]:
                                out_temp[i][col] = 1.0
                            else:
                                out_temp[i][col] = 0.0
                        elif col == (len(col_data) + 5 - 6):
                            if '999.0' in file_lines[row]:
                                out_temp[i][col] = 1.0
                            else:
                                out_temp[i][col] = 0.0
                        else:
                            out_temp[i][col] = col_data[col].split(' ')[i]
                out += out_temp
            else:
                continue
        else:
            labels = file_lines[row].split(',')
            for i in range(5):
                labels.insert(len(labels)-1,'error_'+str(i+1))
            labels = ",".join(labels)
            print(labels)
    return {'data': np.nan_to_num(np.array(out).astype(float)), 'labels': labels}


def save_file(name, obj):
    np.savez_compressed(name, obj['data'])
    pickle.dump(obj['labels'], open(name + ".p", "wb"))


def load_file(name):
    return {'data': np.load(name+'.npz')['arr_0'] ,'labels':pickle.load(open(name + ".p", "rb"))}