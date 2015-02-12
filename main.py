import tools
import time
import numpy as np

if __name__ == '__main__':
    '''
    #Parse Data and Save Data
    data_dict = tools.parse_file('train_2013.csv')
    tools.save_file('train_2013', data_dict)
    np.savetxt("processed_train_2013.csv", data_dict['data'], delimiter=",")
    '''
    data_dict = tools.load_file('train_2013')
    data_dict['pca_data'] = tools.pca_norm(np.nan_to_num(data_dict['data'][1:10000,1:19]), k = 10)
    data_dict['pca_data'].norm()
    print(data_dict['pca_data'].exp_var)
    gen = (i for i,k in zip(range(len(data_dict['pca_data'].exp_var)),data_dict['pca_data'].exp_var) if k*100>90.0)
    print(next(gen)+1)