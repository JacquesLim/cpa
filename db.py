#!/usr/bin/python3
# -*- coding: utf-8 -*-
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

# # 打开数据库连接
# db = pymysql.connect("rm-wz9rw2pr9mox4w6m1go.mysql.rds.aliyuncs.com", "root", "Root@2017", "mysql")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
#
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()