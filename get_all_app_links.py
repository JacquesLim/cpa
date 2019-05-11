#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_all_app_links.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/11 12:03   Jacques Lim    1.0         None
'''
from bs4 import BeautifulSoup
import requests

'''
配置文件路径
all_pages_links_path: 所有需要爬取APPID的有效页面链接
all_app_links_path: 存储所有APP的链接url
'''
all_pages_links_path = 'C:/Users/mayn/Desktop/all_pages_links.txt'
all_app_links_path =  'C:/Users/mayn/Desktop/all_app_links.txt'

def getHtml(url):
    '''
    获取网页
    :param url:
    :return: res
    '''
    retry_count = 5
    while retry_count > 0:
        try:
            html = requests.get(url, timeout=10)
            if len(html.text) > 0:
                return html
            else:
                getHtml(url)

        except Exception:
            retry_count -= 1
    getHtml(url)

def get_links(url,classname):
    '''
    获取一定格式的所有链接
    :param url: 页面url
    :param classname: 类名为classname
    :return: 所有链接列表
    '''
    res = getHtml(url)
    links = []
    try:
        # print("获取的内容是：" + res.text)
        soup = BeautifulSoup(res.text, 'html.parser')
        all_a = soup.find(class_=classname).find_all('a')
        for one_a in all_a:
            link = one_a.get('href')
            links.append(link)
    except:
        # print("获取的HTML内容为空")
        get_links(url, classname)
    return links


if __name__ == "__main__":
    #获取所有APP链接
    all_pages_links = []
    with open(all_pages_links_path, 'r', encoding='utf8')as f:
        all_pages_links = f.read().split('\n')
    for page_link in all_pages_links:
        page_app_links = get_links(page_link, 'grid3-column')
        print('正在爬取的链接：{}'.format(page_link))
        print('此页共有APPID：{}个'.format(len(page_app_links)))
        for page_app_link in page_app_links:
            with open(all_app_links_path, 'a+', encoding='utf8')as f:
                f.write(page_app_link + '\n')