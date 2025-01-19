"""LAST_TO_END  (反映最近一段时间活跃程度) """
import pandas as pd
import Data_Process

origin_data = pd.read_csv('../CSV数据集/solve_air_data.csv', encoding='UTF-8')
card_number_data = origin_data[['会员卡号']]
end_year_data = origin_data[['最后一次乘机时间至观察窗口末端时长']]
activity_level_data = pd.concat([card_number_data, end_year_data], axis=1)
Data_Process_result = Data_Process.Data_Clean(activity_level_data)
Data_Process_result.to_csv('../CSV数据集/activity_level_data.csv', index=False)
