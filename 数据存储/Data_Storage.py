import pandas as pd
import pymysql


def Data_save_mysql(csv_path, create_query, insert_query):
    data = pd.read_csv(csv_path)
    connection = pymysql.connect(host='localhost', user='root', password='123456', database='qmks2023')
    # 数据库连接
    cursor = connection.cursor()
    cursor.execute(create_query)
    # 执行创建数据库表语句
    values = [tuple(row) for row in data.values]
    cursor.executemany(insert_query, values)
    connection.commit()
    cursor.close()
    connection.close()

