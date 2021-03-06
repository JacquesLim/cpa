#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   update_app_similar.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/13 14:37   Jacques Lim    1.0         输出update的sql文件，更新appinfo表里的similar字段
'''
import requests
from db import Database
from bs4 import BeautifulSoup
import re

# APP链接文件路径
app_links_path = './datafile/all_app_links_update.txt'
# 更新数据库sql文件
update_similar_sql_path = './datafile/update_similar_{}.sql'
# log文件
update_app_similar_info_path = './log/update_app_similar_info.log'

def update_app_similar(id):
    url = 'https://itunes.apple.com/cn/app/app/id{}'
    try:
        html = requests.get(url.format(id), timeout=10)
        soup = BeautifulSoup(html.text, 'html.parser')
        str = soup.find(id='shoebox-ember-data-store').text
        index = str.find('customersAlsoBoughtApps')
        com = re.compile(r'"(\d+)"') #匹配“id”
        similar = com.findall(str[index:index+700])
        similar = [ int(x) for x in similar ] #字符串转数字
        table = 'app_info'
        field = "similar='{}'".format(similar)
        condition = 'id={}'.format(id)
        return Database.update_sql(table, field, condition)
    except:
        print('id：{}：爬取失败'.format(id))
        with open(update_app_similar_info_path, 'a+', encoding='utf8')as ff:
            ff.write('id：{}：爬取失败'.format(id))
        return None

if __name__ == "__main__":
    with open(app_links_path, 'r', encoding='utf8')as file:
        n=0
        for line in file:
            n += 1
            id = line.split('/')[6].replace('id', '').replace('?mt=8', '')
            with open(update_similar_sql_path.format(int(n/100000)), 'a+', encoding='utf8')as ff:
                sql = update_app_similar(int(id))
                if sql is not None:
                    ff.write(sql)
            if n%1000 ==0:
                print('正在生成第{}行sql'.format(n))