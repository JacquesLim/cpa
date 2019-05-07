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
from fake_useragent import UserAgent
import random

ips = [
    "196.13.208.23:8080",
    "47.99.113.175:8118",
    "185.82.212.95:8080",
    "219.223.222.6:8123",
    "221.210.120.153:54402",
    "60.205.202.3:3128",
    "87.139.168.220:8080",
    "95.88.12.230:3128",
    "111.198.154.116:8888",
    "94.130.20.85:31288"
    ]

def get_random_header():
    ua = UserAgent()
    header = {
        "User-Agent": ua.random

    }
    print(header)
    return header

def getHtml(url):
    # ....
    retry_count = 5
    while retry_count > 0:
        headers = get_random_header()
        rand_ip = get_proxy_ip()
        proxies = {
            'https': 'https://' + rand_ip
        }

        try:
            html = requests.get(url, headers=headers, proxies=proxies, timeout=10)
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
    print(rand_ip)
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
        print("获取的HTML内容为空")
        get_links(url, classname)
    return links

def get_all_appid(output_ips, output_done, start_term, start_alpha, start_pav):
    '''
    获取APPSTORE 所有APP的APPID
    :param output_ips: 存放APPID的文件路径
    :param output_done: 存放已爬取过的链接的文件路径
    :param start_term: 这些分类已经爬取过，不用再爬了
    :param start_alpha: 这些字母分页已经爬取过了，不用再爬了
    :param start_pav: 这些数字分页已经爬取过了，不用再爬了
    :return: 返回的是该APP的详情页链接URL
    '''
    links=[]
    terms_link = get_links('https://itunes.apple.com/cn/genre/ios/id36?mt=8','grid3-column')
    for term_link in terms_link:
        if term_link.split('/')[6].replace('id', '').replace('?mt=8', '') not in start_term: #检查是否爬过该分类所有链接
            alphabet_links = get_links(term_link,'list alpha')
            # print(len(alphabet_links))
            for alphabet_link in alphabet_links:
                if alphabet_link[-1] >= start_alpha: #检查是否爬过该字母分类所有链接
                    i = start_pav + 1
                    pav_links = []
                    temp_last_link = '' #保存最后一页，最后一个链接的值
                    while(i == start_pav + 1 or (len(pav_links)>0 and temp_last_link!=links[-1])): #排除超过分页仍然是检索出最后一个分页的数据
                        link = alphabet_link + '&page=' + str(i)
                        with open(output_done, 'a+', encoding='utf8')as f:
                            f.write(link + '\n')
                        pav_links = get_links(link, 'grid3-column')
                        for pav_link in pav_links:
                            appid = pav_link.split('/')[6].replace('id', '').replace('?mt=8', '')
                            # print(appid)
                            with open(output_ips,'a+',encoding='utf8')as f:
                                f.write(appid + '\n')
                        temp_last_link = links[-1]  # 保存最后一页，最后一个链接的值
                        links = links + pav_links
                        i = i + 1
                        print('正在爬取页面：' + link)
                        print('已爬取APPID数量：' + str(len(links)))
                    start_pav = 0 #重置分页，下一轮在第1页开始爬
            start_alpha = 'A' #重置分页，下一轮在第A页开始爬
    return links
