#!/usr/bin/python3
# -*- coding: utf-8 -*-

from db import Database
import scrapy

if __name__ == "__main__":
    host = "rm-wz9rw2pr9mox4w6m1go.mysql.rds.aliyuncs.com"
    port = 3306
    user = "root"
    passwd = "Root@2017"
    db = "cpa"
    charset = "utf8"
    cpa = Database(host, port, user, passwd, db, charset)
    dataset = scrapy.scrapy_qimai_search("招标")
    table = dataset[0]
    column = dataset[1]
    datatype = dataset[2]
    value = dataset[3:]
    print(table)
    print(column)
    print(datatype)
    print(value)
    cpa.insert(table, column, datatype, value)