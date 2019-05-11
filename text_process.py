#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   text_process.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/11 13:05   Jacques Lim    1.0         处理各种文本
'''

'''
配置文件路径
all_appid_path_test: 存储所有APPID
all_app_links_path: 存储所有APP的链接url
'''
all_appid_path_test = 'C:/Users/mayn/Desktop/all_appid_test.txt'
all_app_links_path_test =  'C:/Users/mayn/Desktop/all_app_links_test.txt'


def get_appid(text):
    return text.split('/')[6].replace('id', '').replace('?mt=8', '')

with open(all_app_links_path_test, 'r', encoding='utf8')as file:
    n = 0
    for line in file:
        n += 1
        appid = get_appid(line)
        with open(all_appid_path_test, 'a+', encoding='utf8')as f:
            f.write(appid)
        if n%10000 == 0:
            print("已处理{}行".format(n))