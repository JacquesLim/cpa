#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   text_process.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/11 13:05   Jacques Lim    1.0         处理各种文本
'''
import re

'''
配置文件路径
all_appid_path_test: 存储所有APPID
all_app_links_path: 存储所有APP的链接url
'''
all_appid_path_test = './datafile/app_lookup_url.txt'
all_app_links_path_test =  'C:/Users/mayn/Desktop/all_app_links.txt'
genre_letter_pav_links_path = 'C:/Users/mayn/Desktop/genre_letter_pav_links.txt'


def get_lookup_url(text):
    url = "https://itunes.apple.com/lookup?id={}&country=cn&entity=software"
    return url.format(text.split('/')[6].replace('id', '').replace('?mt=8', '').replace('\n',''))

def get_appid(url):
    com = re.compile('id(\d+)?')
    id = com.findall(url)[0]
    return id

def get_last_url(urls, generId, letter):
    s = 'id{}?mt=8&letter={}&page='.format(generId, letter)
    generId_letter_list = []
    for url in urls:
        if s in url:
            generId_letter_list.append('{}-{}:{}'.format(generId, letter, url))
    if len(generId_letter_list)>0:
        return generId_letter_list[-1]
    else:
        return []

def get_genreId(text):
    '''
    这里需要重新处理
    :param text:
    :return:
    '''
    com = re.compile(r'id(\d+)\?')
    all_list = com.findall(text)
    generId_list = list(set(all_list))
    print(generId_list)
    return generId_list


# with open(all_app_links_path_test, 'r', encoding='utf8')as file:
#     n = 0
#     for line in file:
#         n += 1
#         appid = get_appid(line)
#         with open(all_appid_path_test, 'a+', encoding='utf8')as f:
#             f.write(appid + '\n')
#         if n%10000 == 0:
#             print("已处理{}行".format(n))
# letter_list = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                 'U', 'V', 'W', 'X', 'Y', 'Z']
# with open(genre_letter_pav_links_path,'r')as f:
#     text = f.read()
#     urls = text.split()
#     generId_list = get_genreId(text)
#     last_url = []
#     for generId in generId_list:
#         for letter in letter_list:
#             last_url.append(get_last_url(urls,generId,letter))
#     print(last_url)

print(get_appid("https://itunes.apple.com/cn/app/%E9%92%89%E9%92%89/id930368978?mt=8"))