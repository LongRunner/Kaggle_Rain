import numpy as np
import pickle
import time

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
            else:
                print(col_data)
                print(len(col_data))
                print('\n')
                continue
            out_temp = [x[:] for x in [[None] * 20] * (repeat)]
            id_n = float(col_data[0])
            exp_rain = float(col_data[len(col_data) - 1])
            for col in range(len(col_data)):
                for i in range(repeat):
                    if col == 0:
                        out_temp[i][col] = id_n
                    elif col == (len(col_data) - 1):
                        out_temp[i][col] = exp_rain
                    else:
                        out_temp[i][col] = col_data[col].split(' ')[i]
            out += out_temp
        else:
            labels = file_lines[row].split(',')
    return {'data': np.array(out), 'labels': labels}


def save_file(name, object):
    pickle.dump(object, open(name + ".p", "wb"))


def load_file(name):
    return pickle.load(open(name + ".p", "rb"))

if __name__ == '__main__':
    data_dict = parse_file('train_2013.csv')
    save_file('train_2013', data_dict)
