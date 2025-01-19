import numpy as np
import pandas as pd


origin_data = pd.read_csv('../CSV数据集/air_data.csv', encoding='UTF-8')

'''地图大屏的数据清洗'''
selected_city_data = origin_data[['工作地城市', '工作地省份']]
replace_str_data = selected_city_data.replace(to_replace='.', value=np.nan)
no_str_data = replace_str_data.dropna(how='any')
replace_English_data = no_str_data.replace(to_replace='[a-zA-Z]', value=np.nan, regex=True)  # 去除海外城市
no_null_data = replace_English_data.dropna(how='any')
no_null_data.to_csv('../CSV数据集/map_city_data.csv', index=False, encoding='UTF-8')

