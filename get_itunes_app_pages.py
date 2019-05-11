#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_itunes_app_pages.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/11 11:37   Jacques Lim    1.0         None
'''
from bs4 import BeautifulSoup
import requests

'''
配置文件路径
genre_links_path : 记录各个分类热门APP链接
genre_letters_links_path: 记录各个分类字母分类链接
genre_letters_pavs_links_path: 记录各个分类字母分类下各个分页的链接
'''
genre_links_path = 'C:/Users/mayn/Desktop/genre_links.txt'
genre_letters_links_path = 'C:/Users/mayn/Desktop/genre_letter_links.txt'
genre_letters_pavs_links_path = 'C:/Users/mayn/Desktop/genre_letter_pav_links.txt'

def getHtml(url):
    # ....
    retry_count = 5
    while retry_count > 0:
        try:
            html = requests.get(url, timeout=10)
            # html = requests.get(url, timeout=10)
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

alphabet = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']


def get_pav_last_default_links(link):
    '''
    用于处理每个分类下最后一页的数据，记录初始值
    :param link: 每个分类字母的链接
    :return: 返回最后一页的链接数据，最后一页和最后300页的数据是一样的
    '''
    url = link + '&page=300'
    return get_links(url, 'grid3-column')
def get_pagecount(url, start, end):
    '''
    找到每个字母分页下共有多少数字分页
    :param url: 需要分析的链接
    :param start: 开始页数
    :param end: 结束页数
    :return: 最终页数
    '''
    p = start + int((end - start) / 2)
    links = get_links('{}&page={}'.format(url, p), 'grid3-column')
    pav_last_default_links = get_pav_last_default_links(url)
    # print('{}~{}'.format(start, end))
    if links == pav_last_default_links and (end - start) > 1:
        return get_pagecount(url, start, p)

    elif links != pav_last_default_links and (end - start) > 1:
        return get_pagecount(url, p, end)
    else:
        return p


if __name__ == "__main__":
    #获取所有包含iOS APP的页面链接
    genre_links = get_links('https://itunes.apple.com/cn/genre/ios/id36?mt=8','grid3-column')
    genre_letter_links = []
    for genre_link in genre_links:
        with open(genre_links_path, 'a+', encoding='utf8')as f:  #记录各个分类热门APP链接
            f.write(genre_link + '\n')
        for letter in alphabet:
            link = genre_link + '&letter=' + letter
            with open(genre_letters_links_path, 'a+', encoding='utf8')as f: #记录各个分类字母分类链接
                f.write(link + '\n')
            genre_letter_links.append(link)
    print(len(genre_letter_links))
    for genre_letter_link in genre_letter_links:
        start = 0
        end = get_pagecount(genre_letter_link, 0, 200)
        print(genre_letter_link)
        print('总页数：{}'.format(end))
        for i in range(1,end+1):
            genre_letter_pav_link = genre_letter_link + '&page={}'.format(i)
            with open(genre_letters_pavs_links_path, 'a+', encoding='utf8')as f: #记录各个分类字母分类下各个分页的链接
                f.write(genre_letter_pav_link + '\n')
