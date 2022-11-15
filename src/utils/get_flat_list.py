
from typing import List
import re


def get_unique_sorted_values_from_list(values_list: List[str]) -> List[str]:

    list_flattened = []
    cleaned_list = [x for x in values_list if str(x) != 'nan']
    for item in cleaned_list:
        items_flattened = re.split(r', \s*', item)
        list_flattened.extend(items_flattened)

    return sorted(set(list_flattened))
