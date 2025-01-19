import Data_Storage

'''1地图大屏数据的存储'''
Data_Storage.Data_save_mysql(csv_path='../CSV数据集/map_city_data.csv',
                             create_query="""
CREATE TABLE IF NOT EXISTS `hxh2491` (
    `工作地城市` VARCHAR(255),
    `工作地省份` VARCHAR(255)
)
""", insert_query="INSERT INTO `hxh2491` (`工作地城市`, `工作地省份`) VALUES (%s, %s)")

'''2源数据的存储(air_data.csv)'''
Data_Storage.Data_save_mysql(csv_path='../CSV数据集/solve_air_data.csv',
                             create_query="""
CREATE TABLE IF NOT EXISTS `hxh2492` (
    `编号` INT(11),
    `会员卡号` INT(11),
    `入会时间` DATE,
    `第一次飞行日期` DATE,
    `性别` CHAR(1),  -- 如果性别只有两个取值，可以使用 CHAR(1) 或 ENUM('M', 'F')
    `会员卡级别` VARCHAR(255),
    `工作地城市` VARCHAR(255),
    `工作地省份` VARCHAR(255),
    `工作地国家` VARCHAR(255),
    `年龄` INT(11),
    `观测窗口的结束时间` DATE,
    `飞行次数` INT(11),
    `观测窗口总基本积分` INT(11),
    `第一年精英资格积分` INT(11),
    `第二年精英资格积分` INT(11),
    `第一年总票价` DECIMAL(10, 2),  -- 根据实际情况调整精度和范围
    `第二年总票价` DECIMAL(10, 2),
    `观测窗口总飞行公里数` INT(11),
    `观察窗口总加权飞行公里数` INT(11),
    `观测窗口季度平均飞行次数` DECIMAL(10, 2),
    `观测窗口季度平均基本积分累积` INT(11),
    `观察窗口内第一次乘积时间至MAX` INT(11),
    `最后一次乘机时间至观察窗口末端时长` INT(11),
    `平均乘机时间间隔` DECIMAL(10, 2),
    `观察窗口内最大乘机间隔` INT(11),
    `观测窗口中第1年其他积分` INT(11),
    `观测窗口中第2年其他积分` INT(11),
    `积分兑换次数` INT(11),
    `平均折扣率` DECIMAL(4, 2),
    `第1年乘机次数` INT(11),
    `第2年乘机次数` INT(11),
    `第1年里程积分` INT(11),
    `第2年里程积分` INT(11),
    `观测窗口总精英积分` INT(11),
    `观测窗口中其他积分` INT(11),
    `非乘机积分综合` INT(11),
    `第2年非乘机积分总和` INT(11),
    `总累计积分` INT(11),
    `第2年观测窗口总累计积分` INT(11),
    `第2年的乘机次数比率` DECIMAL(4, 2),
    `第1年的乘机次数比率` DECIMAL(4, 2),
    `第1年的运输比率` DECIMAL(4, 2),
    `第2年的运输比率` DECIMAL(4, 2),
    `没有乘机的积分` INT(11)
)
""", insert_query="INSERT INTO `hxh2492` (`编号`,`会员卡号`,`入会时间`,`第一次飞行日期`,`性别`,`会员卡级别`," \
                  "`工作地城市`,`工作地省份`,`工作地国家`,`年龄`,`观测窗口的结束时间`,`飞行次数`,`观测窗口总基本积分`,`第一年精英资格积分`," \
                  "`第二年精英资格积分`,`第一年总票价`,`第二年总票价`,`观测窗口总飞行公里数`,`观察窗口总加权飞行公里数`," \
                  "`观测窗口季度平均飞行次数`,`观测窗口季度平均基本积分累积`,`观察窗口内第一次乘积时间至MAX`,`最后一次乘机时间至观察窗口末端时长`," \
                  "`平均乘机时间间隔`,`观察窗口内最大乘机间隔`,`观测窗口中第1年其他积分`,`观测窗口中第2年其他积分`,`积分兑换次数`,`平均折扣率`,`第1年乘机次数`," \
                  "`第2年乘机次数`,`第1年里程积分`,`第2年里程积分`,`观测窗口总精英积分`,`观测窗口中其他积分`,`非乘机积分综合`,`第2年非乘机积分总和`," \
                  "`总累计积分`,`第2年观测窗口总累计积分`,`第2年的乘机次数比率`,`第1年的乘机次数比率`,`第1年的运输比率`,`第2年的运输比率`,`没有乘机的积分`) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s" \
                  ",%s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)")

"""3city_active_time.csv数据存储"""
Data_Storage.Data_save_mysql(csv_path='../CSV数据集/city_active_time_data.csv',
                             create_query="""
CREATE TABLE IF NOT EXISTS `hxh2493` (
    `工作地城市` VARCHAR(255),
    `乘客活跃时间` VARCHAR(255)
)
""", insert_query="INSERT INTO `hxh2493` (`工作地城市`, `乘客活跃时间`) VALUES (%s, %s)")

"""4activity_level_data.csv数据存储"""
Data_Storage.Data_save_mysql(csv_path='../CSV数据集/activity_level_data.csv',
                             create_query="""
CREATE TABLE IF NOT EXISTS `hxh2494` (
    `会员卡号` VARCHAR(255),
    `最后一次乘机时间至观察窗口末端时长` int(11)
)
""", insert_query="INSERT INTO `hxh2494` (`会员卡号`, `最后一次乘机时间至观察窗口末端时长`) VALUES (%s, %s)")

"""5sex_age_fly_data.csv数据存储"""
Data_Storage.Data_save_mysql(csv_path='../CSV数据集/sex_age_fly_data.csv',
                             create_query="""
CREATE TABLE IF NOT EXISTS `hxh2495` (
    `性别` VARCHAR(255),
    `平均年龄` float(11),
    `平均飞行次数` float(11)
)
""", insert_query="INSERT INTO `hxh2495` (`性别`, `平均年龄`,`平均飞行次数`) VALUES (%s, %s, %s)")

"""6sex_time_kilo_data.csv数据存储"""
Data_Storage.Data_save_mysql(csv_path='../CSV数据集/sex_time_kilo_data.csv',
                             create_query="""
CREATE TABLE IF NOT EXISTS `hxh2496` (
    `性别` VARCHAR(255),
    `平均乘机时间间隔` float(11),
    `平均总飞行公里数` float(11)
)
""", insert_query="INSERT INTO `hxh2496` (`性别`, `平均乘机时间间隔`,`平均总飞行公里数`) VALUES (%s, %s, %s)")

"""7card_level_discount_data数据存储"""
Data_Storage.Data_save_mysql(csv_path='../CSV数据集/card_level_discount_data.csv',
                             create_query="""
CREATE TABLE IF NOT EXISTS `hxh2497` (
    `会员卡级别` int(11),
    `平均折扣率` float(11)
    
)
""", insert_query="INSERT INTO `hxh2497` (`会员卡级别`, `平均折扣率`) VALUES (%s, %s)")

"""8total_cum_points_data数据存储"""
Data_Storage.Data_save_mysql(csv_path='../CSV数据集/total_cum_points_data.csv',
                             create_query="""
CREATE TABLE IF NOT EXISTS `hxh2498` (
    `会员卡号` VARCHAR(255),
    `总累计积分` int(11)
)
""", insert_query="INSERT INTO `hxh2498` (`会员卡号`, `总累计积分`) VALUES (%s, %s)")

