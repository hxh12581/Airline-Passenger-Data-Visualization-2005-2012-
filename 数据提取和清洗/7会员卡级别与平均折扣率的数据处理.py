import pandas as pd
import Data_Process

origin_data = pd.read_csv('../CSV数据集/solve_air_data.csv', encoding='UTF-8')
member_card_level = origin_data[['会员卡级别']]
mean_discount_rate = origin_data[['平均折扣率']]
card_level_discount_data = pd.concat([member_card_level, mean_discount_rate], axis=1)
Data_Process_result = Data_Process.Data_Clean(card_level_discount_data)
card_level_discount_data = Data_Process_result.groupby('会员卡级别')[['平均折扣率']].mean()
card_level_discount_data.reset_index(inplace=True)
card_level_discount_data.to_csv('../CSV数据集/card_level_discount_data.csv', index=False)
