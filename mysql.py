import pymysql
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType, RenderType, ThemeType

host = 'localhost'
port = 3306
user = 'root'
pwd = '123456'
dbName = 'qmks2023'


class Mysql:
    def __init__(self, host=host, port=port, user=user, pwd=pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        pass

    # 打开数据库连接  第一个步骤
    def openConn(self, db):
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.pwd, database=db,
                                    charset='utf8')
        return self.conn.cursor()

    # 查看是否存在该表
    def isTable(self, tName):
        flag = -1
        try:
            cur = self.openConn(dbName)
            flag = cur.execute("select table_name from information_schema.tables where table_name='" + tName + "'")
        except pymysql.Error as e:
            print(str(e))
        finally:
            self.closeConn()
        return flag

    # 数据库查询操作
    def selectSQL(self, strSql):
        list = None
        try:
            # 1 打开数据库连接
            cur = self.openConn(db=dbName)
            # 2 数据库查询操作
            cur.execute(strSql)  # 返回值 行数
            list = cur.fetchall()
            # 3 关闭游标
            cur.close()
        except pymysql.Error as e:
            print(str(e))
        finally:
            # 3 关闭数据连接
            self.closeConn()
        return list

    # 修改数据库记录
    def update(self, strSql):
        num = -1  # sql 语法错误
        try:
            # 1 打开数据库连接
            cur = self.openConn(db=dbName)
            # 2 数据库修改操作
            num = cur.execute(strSql)  # 修改的行数
            self.conn.commit()  # 修改操作完成后必须提交
            # 3 关闭游标
            cur.close()
        except pymysql.Error as e:
            print(str(e))
        finally:
            # 3 关闭数据连接
            self.closeConn()
        return num

    # 批量修改数据库记录  (事务处理)
    def updateList(self, listSql):
        try:
            # 1 打开数据库连接
            cur = self.openConn(db=dbName)
            # 2 数据库修改操作
            for strSql in listSql:
                cur.execute(strSql)  # 修改的行数
            self.conn.commit()  # 修改操作完成后必须提交
            # 3 关闭游标
            cur.close()
        except pymysql.Error as e:
            print(str(e))
            self.conn.rollback()  # 回滚
        finally:
            # 3 关闭数据连接
            self.closeConn()

    # 关闭数据库连接
    def closeConn(self):
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    my = Mysql(host=host, port=port, user=user, pwd=pwd)
    # #打开数据库连接
    # cur=my.openConn(dbName)
    # if cur:
    #     print('已打开数据库')
    #     cur.close()
    #     my.closeConn()
    #     print('关闭数据库连接')
    # strsql="update student set stuAge=19 where stuId='20210101'"
    # print(my.update(strSql=strsql))
    # strsql="insert into student(stuId,stuName,stuAge,stuSex,bjId,ruxue,pwd) values('20220103','lisi',18,'M',3,2022,'123')"
    # print(my.update(strSql=strsql))
    # strsql="delete from student where stuId='20220102'"
    # print(my.update(strSql=strsql))
    # strSql="select * from student"
    # list=my.selectSQL(strSql=strSql)
    # for l in list:
    #     print(l)
    # 修改 stus
    # if my.isTable('stus') == 0:
    #     # 创建表格
    #     strsql = '''
    #     create table stus(
    #         id char(8) primary key,
    #         name varchar(20) not null,
    #         age int default 18
    #     ) default charset=utf8;
    #     '''
    #     print(my.update(strsql))
