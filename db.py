#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   ttt.py
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/4/25 16:39   Jacques Lim    1.0         用于数据库连接
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

    def insert(self, table, column, datatype, value):
        '''
        向数据表table插入数据
        :param table: 数据表名
        :param column: 字段
        :param datatype: 字段数据类型
        :param value: 插入的值
        :return:
        '''
        sql = 'insert into ' + table + str(column) + ' values' + str(datatype) + ';'
        print(sql)
        self.cursor.executemany(sql, value)
        self.connect.commit()

    @staticmethod
    def insert_sql(table, column, values):
        '''
        生成批量插入sql
        :param table: 数据表名
        :param column: 字段
        :param value: 插入的值列表[(),(),()]
        :return:
        '''
        sql = 'insert into {}{} values {};'
        for v in  values:
            sql = sql.format(table,column,v)
        return sql

    @staticmethod
    def update_sql(table, field, condition):
        sql = 'update {} SET {} where {};'.format(table, field, condition)
        return sql

    def select_latest_record_date(self, appid):
        '''
        根据appid 查询表app_record最后更新时间
        :param appid:
        :return: 最后更新时间
        '''
        sql = 'select app_date from app_record where app_id=' + str(appid) + ' order by app_date desc limit 1;'
        print(sql)
        try:
            print("正在查询APPID:" + str(appid))
            self.cursor.execute(sql)
            result = self.cursor.fetchone()[0]
        except:
            print("该APPID:" + str(appid) + "没有任何数据")
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
