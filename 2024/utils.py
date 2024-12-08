import os
from typing import Any

import pandas as pd
import numpy as np


def load_data(file_name: str):
    """
    Load data for each riddle
    :param file_name: name of the file to load e.g. "day_1.txt"
    :type file_name: str
    :return: data as np.array or pd.DataFrame values
    """
    file_path = os.path.join(file_name)
    try:
        return np.loadtxt(file_path)
    except:
        data = pd.read_csv(file_path, header=None)
        return data.values
