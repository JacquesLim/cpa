#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   ttt.py
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/4/25 16:39   Jacques Lim    1.0         None
'''

import pymysql

class Database:
    def __init__(self, host, port, user, passwd, db, charset):
        connect = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            db=db,
            charset=charset
        )
        cursor = connect.cursor()
        self.connect = connect
        self.cursor = cursor

    # 定义要执行的sql语句
    def insert(self, table, column, datatype, value):
        sql = 'insert into ' + table + str(column) + ' values' + str(datatype) + ';'
        print(sql)
        self.cursor.executemany(sql, value)
        self.connect.commit()

    def select_latest_record_date(self, appid):
        sql = 'select app_date from app_record where app_id=' + str(appid) + ' order by app_date desc limit 1;'
        print(sql)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()[0]
        except:
            print("该APPID没有任何数据")
            result = ""
        return result

    def select_all_app(self):
        sql = 'select * from app_info group by app_id order by date desc;'
        print(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
        except:
            print("查询失败")
            results = ""
        return results

# 数据库字段声明
host = "rm-wz9rw2pr9mox4w6m1go.mysql.rds.aliyuncs.com"
port = 3306
user = "root"
passwd = "Root@2017"
db = "cpa"
charset = "utf8"
cpa = Database(host, port, user, passwd, db, charset)
print(cpa.select_all_app())