#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("rm-wz9rw2pr9mox4w6m1go.mysql.rds.aliyuncs.com", "root", "Root@2017", "mysql")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 定义要执行的sql语句

sql = 'insert into userinfo(user,pwd) values(%s,%s);'
data = [
    ('july', '147'),
    ('june', '258'),
    ('marin', '369')
]

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()