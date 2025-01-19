import pandas as pd
import Data_Process

origin_data = pd.read_csv('../CSV数据集/solve_air_data.csv', encoding='UTF-8')
sex = origin_data[['性别']]
age = origin_data[['年龄']]
fly_count = origin_data[['飞行次数']]
sex_age_fly_data = pd.concat([sex, age, fly_count], axis=1)
Data_Process_result = Data_Process.Data_Clean(sex_age_fly_data)
sex_age_fly_data = Data_Process_result.groupby('性别')[['年龄', '飞行次数']].mean()
sex_age_fly_data.reset_index(inplace=True)  # 将分组后的index性别重新设置为一个新的列
sex_age_fly_data.rename(columns={'年龄': '平均年龄', '飞行次数': '平均飞行次数'}, inplace=True)  # 修改列名
sex_age_fly_data.to_csv('../CSV数据集/sex_age_fly_data.csv', index=False)
