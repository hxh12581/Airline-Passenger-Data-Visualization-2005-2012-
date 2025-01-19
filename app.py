from flask import Flask, render_template

from mysql import Mysql

app = Flask(__name__)


@app.route('/')
def index():
    m = Mysql()
    # 1.地图数据
    map_data_result = m.selectSQL(
        "SELECT 工作地城市, COUNT(*)/50 as 城市数量 FROM hxh2491 GROUP BY 工作地城市 HAVING COUNT(*) ORDER BY 城市数量 DESC LIMIT 30;")
    map_city = [md[0] for md in map_data_result]
    map_count = [md[1] for md in map_data_result]
    # 2.2005-2012期间乘客平均年龄和平均出行次数
    sex_age_fly_data_result = m.selectSQL("SELECT 平均年龄,平均飞行次数 FROM `hxh2495`")
    mean_age = [saf[0] for saf in sex_age_fly_data_result]
    mean_fly_count = [saf[1] for saf in sex_age_fly_data_result]
    # 3.2005-2012年期间排名前10的城市乘客活跃总时长的数据
    sql_query = """
    SELECT 
        CASE 
            WHEN 工作地城市 LIKE '%市' THEN REPLACE(工作地城市, '市', '') 
            ELSE 工作地城市 
        END AS 工作地城市处理,
        SUM(乘客活跃时间) AS 活跃时间总和
    FROM 
        hxh2493
    GROUP BY 
        工作地城市处理
    ORDER BY 
        活跃时间总和 DESC
    LIMIT 10;
    """
    city_active_time_data_result = m.selectSQL(sql_query)
    active_city = [catd[0] for catd in city_active_time_data_result]
    active_days = [catd[1] for catd in city_active_time_data_result]
    # 4.2005-2012年期间不同活跃程度区间内的乘客数量占比
    sql_query_pie = """SELECT 
    CASE
        WHEN 最后一次乘机时间至观察窗口末端时长 BETWEEN 0 AND 99 THEN '0-99'
        WHEN 最后一次乘机时间至观察窗口末端时长 BETWEEN 100 AND 199 THEN '100-199'
        WHEN 最后一次乘机时间至观察窗口末端时长 BETWEEN 200 AND 299 THEN '200-299'
        WHEN 最后一次乘机时间至观察窗口末端时长 BETWEEN 300 AND 399 THEN '300-399'
        WHEN 最后一次乘机时间至观察窗口末端时长 BETWEEN 400 AND 499 THEN '400-499'
        WHEN 最后一次乘机时间至观察窗口末端时长 BETWEEN 500 AND 599 THEN '500-599'
        WHEN 最后一次乘机时间至观察窗口末端时长 BETWEEN 600 AND 700 THEN '600-700'
				WHEN 最后一次乘机时间至观察窗口末端时长 BETWEEN 700 AND 800 THEN '700-800'
    END AS 时间区间,
    COUNT(DISTINCT 会员卡号) AS 卡号数量
FROM hxh2494
WHERE 最后一次乘机时间至观察窗口末端时长 <= 800
GROUP BY 时间区间
ORDER BY 卡号数量 DESC;"""
    activity_level_data_result = m.selectSQL(sql_query_pie)
    active_time = [ald[0] for ald in activity_level_data_result]
    active_card = [ald[1] for ald in activity_level_data_result]
    # 5.2005-2012期间乘客平均乘机时间间隔和平均总飞行公里数
    sex_time_kilo_data_result = m.selectSQL(
        "SELECT 平均乘机时间间隔,平均总飞行公里数 / 100 as 公里数优化 FROM `hxh2496`")
    mean_time = [stk[0] for stk in sex_time_kilo_data_result]
    mean_kilo = [stk[1] for stk in sex_time_kilo_data_result]
    # 6.2005-2012期间乘客会员级别与平均折扣率之间的关系
    card_level_discount_data_result = m.selectSQL("SELECT 会员卡级别,平均折扣率 FROM `hxh2497`")
    member_card_level = [cld[0] for cld in card_level_discount_data_result]
    mean_discount_rate = [cld[1] for cld in card_level_discount_data_result]
    # 7.2005-2012年期间不同总累计积分区间内的乘客数量占比
    sql_query_pie_1 = """SELECT 
        CASE
            WHEN 总累计积分 BETWEEN 0 AND 50000 THEN '0-50000'
            WHEN 总累计积分 BETWEEN 50001 AND 100000 THEN '50001-100000'
            WHEN 总累计积分 BETWEEN 100001 AND 200000 THEN '100001-200000'
            WHEN 总累计积分 BETWEEN 200001 AND 300000 THEN '200001-300000'
            WHEN 总累计积分 BETWEEN 300001 AND 400000 THEN '300001-400000'
        END AS 总累计积分区间,
        COUNT(DISTINCT 会员卡号) AS 卡号数量
    FROM hxh2498
    WHERE 总累计积分 <= 500000
    GROUP BY 总累计积分区间
    ORDER BY 卡号数量 DESC;"""
    total_cum_points_data_result = m.selectSQL(sql_query_pie_1)
    total_points = [tcp[0] for tcp in total_cum_points_data_result]
    total_card = [tcp[1] for tcp in total_cum_points_data_result]

    # 8.2005-2012年期间乘客总访问量和乘客总飞行次数
    people_count = m.selectSQL("SELECT COUNT(会员卡号) FROM `hxh2492` ")
    fly_count = m.selectSQL("SELECT SUM(飞行次数) FROM `hxh2492` ")
    return render_template('index.html'
                           , map_data=[map_city, map_count]
                           , draw_data_1=[mean_age, mean_fly_count]
                           , draw_data_2=[active_city, active_days]
                           , draw_data_3=[active_time, active_card]
                           , draw_data_4=[mean_time, mean_kilo]
                           , draw_data_5=[member_card_level, mean_discount_rate]
                           , draw_data_6=[total_points, total_card]
                           , mid_data=[people_count, fly_count]
                           )


if __name__ == '__main__':
    app.run()
