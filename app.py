#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   ttt.py
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/4/25 16:39   Jacques Lim    1.0         None
'''
from bs4 import BeautifulSoup
import requests
def get_links(url,classname):
    '''
    获取一定格式的链接
    :param url: 页面url
    :param classname: 类名为classname
    :return: 所有链接列表
    '''
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_a = soup.find(class_=classname).find_all('a')
    links = []
    for one_a in all_a:
        link = one_a.get('href')
        links.append(link)
    return links



# print(get_links('https://itunes.apple.com/cn/genre/ios/id36?mt=8','grid3-column'))

links=[]
terms_link = get_links('https://itunes.apple.com/cn/genre/ios/id36?mt=8','grid3-column')
f = open('C:/Users/mayn/Desktop/appid.txt','a')
for term_link in terms_link:
    alphabet_links = get_links(term_link,'list alpha')
    # print(len(alphabet_links))
    for alphabet_link in alphabet_links:
        i=1
        pav_links = []
        while(i==1 or len(pav_links)>0):
            link = alphabet_link + '&page=' + str(i)
            pav_links = get_links(link, 'grid3-column')
            for pav_link in pav_links:
                appid = pav_link.split('/')[6].replace('id', '').replace('?mt=8', '')
                print(appid)
                f.write(appid + '\n')
            links = links + pav_links
            i = i + 1
            print(link)
            print(len(links))
            # print(len(pav_links))


# print(len(links))
# url = 'https://itunes.apple.com/cn/app/tim-innovation-forum/id1439629578?mt=8'
# appid = url.split('/')[6].replace('id','').replace('?mt=8','')
# print(appid)