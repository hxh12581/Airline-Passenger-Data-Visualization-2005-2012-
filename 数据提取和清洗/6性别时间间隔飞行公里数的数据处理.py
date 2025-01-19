import pandas as pd
import Data_Process

origin_data = pd.read_csv('../CSV数据集/solve_air_data.csv', encoding='UTF-8')
sex = origin_data[['性别']]
time = origin_data[['平均乘机时间间隔']]
fly_kilo = origin_data[['观测窗口总飞行公里数']]
sex_time_kilo_data = pd.concat([sex, time, fly_kilo], axis=1)
Data_Process_result = Data_Process.Data_Clean(sex_time_kilo_data)
sex_time_kilo_data = Data_Process_result.groupby('性别')[['平均乘机时间间隔', '观测窗口总飞行公里数']].mean()
sex_time_kilo_data.reset_index(inplace=True)  # 将分组后的index性别重新设置为一个新的列
sex_time_kilo_data.rename(columns={'平均乘机时间间隔': '平均乘机时间间隔', '观测窗口总飞行公里数': '平均总飞行公里数'},
                          inplace=True)  # 修改列名
sex_time_kilo_data.to_csv('../CSV数据集/sex_time_kilo_data.csv', index=False)
