import numpy as np
import pandas as pd


# 数据清洗
def Data_Clean(data):
    to_replace_list = ['.', '   ', ' ', '-', '0']  # 要删除的冗余元素
    value_list = [np.nan, np.nan, np.nan, np.nan, np.nan]  # 补全元素
    replace_str_data = data.replace(to_replace=to_replace_list, value=value_list)  # 替换
    no_str_data = replace_str_data.dropna(how='any')  # 删除
    return no_str_data
