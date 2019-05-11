#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_all_app_links_https.py
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/11 12:03   Jacques Lim    1.0         该文件相比get_all_app_links.py增加了伪装头部和代理IP
'''
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import random

'''
配置文件路径
all_pages_links_path: 所有需要爬取APPID的有效页面链接
all_app_links_path: 存储所有APP的链接url
'''
all_pages_links_path = 'C:/Users/mayn/Desktop/all_pages_links.txt'
all_app_links_path =  'C:/Users/mayn/Desktop/all_app_links.txt'

ips = [
  "49.51.86.2:3128",
  "123.59.47.5:8080",
  "120.78.141.110:3128",
  "119.101.116.95:9999",
  "61.128.208.94:3128",
  "112.87.69.142:9999",
  "112.85.128.247:9999",
  "59.38.62.100:9797",
  "95.88.12.230:3128",
  "202.101.96.115:1080",
  "113.247.252.114:9090",
  "118.25.40.97:80",
  "112.87.71.73:9999"
]


def get_random_header():
    ua = UserAgent()
    header = {
        "User-Agent": ua.random

    }
    # print(header)
    return header

def getHtml(url):
    '''
    获取网页
    :param url:
    :return: res
    '''
    retry_count = 5
    while retry_count > 0:
        headers = get_random_header() #爬取有效链接时不用
        rand_ip = get_proxy_ip() #爬取有效链接时不用
        proxies = {
            'http': 'http://' + rand_ip
            # 'https': 'https://' + rand_ip
        }

        try:
            html = requests.get(url, headers=headers, proxies=proxies, timeout=10)
            # html = requests.get(url, timeout=10)
            if len(html.text) > 0:
                return html
            else:
                getHtml(url)

        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    ips.remove(rand_ip)
    print('剩余可用IP数量：'+str(len(ips)))
    getHtml(url)

def get_proxy_ip():
    rand_ip = random.choice(ips)
    # print(rand_ip)
    return rand_ip

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