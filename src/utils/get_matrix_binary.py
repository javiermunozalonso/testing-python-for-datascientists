
from typing import List
from pandas import DataFrame


def get_matrix_binary(data: List, list_flattened: List) -> DataFrame:
    binary_matrix = [[0] * 0 for _ in range(len(set(list_flattened)))]

    for data_item in data:
        for i, list_flattened_item in enumerate(list_flattened):
            if list_flattened_item in data_item:
                binary_matrix[i].append(1.0)
            else:
                binary_matrix[i].append(0.0)
    return DataFrame(binary_matrix).transpose()
