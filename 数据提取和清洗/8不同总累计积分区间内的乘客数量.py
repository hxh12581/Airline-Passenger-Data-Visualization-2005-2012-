import pandas as pd
import Data_Process

origin_data = pd.read_csv('../CSV数据集/solve_air_data.csv', encoding='UTF-8')
card_number_data = origin_data[['会员卡号']]
total_cum_points = origin_data[['总累计积分']]
total_cum_points_data = pd.concat([card_number_data, total_cum_points], axis=1)
Data_Process_result = Data_Process.Data_Clean(total_cum_points_data)
Data_Process_result.to_csv('../CSV数据集/total_cum_points_data.csv', index=False)
