#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   mondb.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/11 11:47   Jacques Lim    1.0         用于获取存在数据库mongodb的代理IP，配合proxy_pool使用
'''

import pymongo

class Database:
    def __init__(self, host, db, table):
        self.myclient = pymongo.MongoClient(host)
        self.mydb = self.myclient[db]
        self.mycol = self.mydb[table]

    def get_one(self, name):
        result = self.mycol.find_one()
        return result[name]

    def del_one(self, index, value):
        myquery = {index: value}
        self.mycol.delete_one(myquery)

db = Database('127.0.0.1', 'proxy', 'useful_proxy')
print(db.get_one('proxy'))
