import pandas as pd
import Data_Process
'''源数据的清洗'''
origin_data = pd.read_csv('../CSV数据集/air_data.csv', encoding='UTF-8')
origin_data.drop('末次飞行日期', axis=1, inplace=True)  # 由于末次飞行日期列的数据不符合日期规范 2014年2月日期有误，故删除
Data_Process_result = Data_Process.Data_Clean(origin_data)
Data_Process_result.to_csv('../CSV数据集/solve_air_data.csv', index=False, encoding='UTF-8')
