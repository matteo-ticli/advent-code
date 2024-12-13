import os

import pandas as pd
import numpy as np


def load_array(file_name: str):
    file_path = os.path.join(file_name)
    return np.loadtxt(file_path)

def load_csv(file_name: str):
    data = pd.read_csv(file_name, header=None)
    return data.values

def load_txt(file_name: str, one_line: bool = True):
    if one_line:
        with open(file_name, 'r') as file:
            data = file.read().rstrip()
    else:
        with open(file_name, 'r') as f:
            data = f.read()
    return data
