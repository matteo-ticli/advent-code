import numpy as np
from utils import load_data


def day_1_1(file_name):
    data = load_data(file_name)
    col_0, col_1 = data[:, 0], data[:, 1]
    col_0_sort, col_1_sort = np.sort(col_0), np.sort(col_1)
    cum_sum = np.cumsum(np.abs(col_1_sort - col_0_sort))
    return int(cum_sum[-1])


def day_1_2(file_name):
    data = load_data(file_name)
    col_0, col_1 = data[:, 0], data[:, 1]
    unique, counts = np.unique(col_1, return_counts=True)
    col_1_occurrence_dict = dict(zip(unique, counts))
    collector = [i * col_1_occurrence_dict.get(int(i), 0) for i in col_0]
    return int(sum(collector))


print(f'Solution 1.1 : {day_1_1("day_1.txt")}')
print(f'Solution 1.2 : {day_1_2("day_1.txt")}')
