import pandas as pd
import Data_Process

origin_data = pd.read_csv('../CSV数据集/solve_air_data.csv', encoding='UTF-8')
origin_data['观测窗口的结束时间'] = pd.to_datetime(origin_data['观测窗口的结束时间'])
origin_data['入会时间'] = pd.to_datetime(origin_data['入会时间'])
# 不同城市人群的活跃时长=结束时间-入会时间
origin_data['活跃时间'] = origin_data['观测窗口的结束时间'] - origin_data['入会时间']
city_data = origin_data[['工作地城市']]
origin_data['活跃时间'] = pd.to_timedelta(origin_data['活跃时间']).dt.days  # 计算活跃时间的天数
active_time = origin_data[['活跃时间']]
city_active_time_data = pd.concat([city_data, active_time], axis=1)  # 拼接合并
Data_Process_result = Data_Process.Data_Clean(city_active_time_data)
Data_Process_result.to_csv('../CSV数据集/city_active_time_data.csv', index=False)
