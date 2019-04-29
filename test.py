#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   ttt.py
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/4/25 16:39   Jacques Lim    1.0         None
'''
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
driver_url = r"C:\Users\mayn\AppData\Local\Google\Chrome\Application\chromedriver.exe"
# driver_url = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

def scrapy_qimai_app_search(appid):
    '''
    在网页https://www.qimai.cn/app/version/appid/ 搜索APP ID，并返回APP相关信息
    :param appid:
    :return:
    '''
    browser = webdriver.Chrome(executable_path=driver_url)
    browser.get("https://www.qimai.cn/app/version/appid/"+str(appid)+"/country/cn")
    time.sleep(3)
    global app_data
    global app_name, app_subtitle, app_version, app_date, app_log, app_desc, app_imgurl
    global soup
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    app_data = ["app_record",
                "(app_id, app_name, app_subtitle, app_version, app_date, app_log, app_desc, app_imgurl)",
                "(%s, %s, %s, %s, %s, %s, %s, %s)"]
    def get_page_data():
        '''
        复用获取页面数据功能函数
        :return:
        '''
        app_name, app_subtitle, app_version, app_date, app_log, app_desc, app_imgurl = [""] * 7
        record_lists = soup.find('ul', class_="record-list").find_all('li')
        for record_list in record_lists:
            if (record_list.find('p', class_="version") is not None):
                if (record_list.find('p', class_="version") is not None):
                    app_version = record_list.find('p', class_="version").text.replace("版本：", "")
                if (record_list.find('p', class_="date") is not None):
                    app_date = record_list.find('p', class_="date").text
                if (record_list.find('p', class_="name") is not None):
                    app_name = record_list.find('p', class_="name").text
                if (record_list.find('p', class_="app-name") is not None):
                    app_name = record_list.find('p', class_="app-name").text
                if (record_list.find('p', class_="subtitle") is not None):
                    app_subtitle = record_list.find('p', class_="subtitle").text

                desc = record_list.find_all(class_="description")
                if (len(desc) > 0):
                    app_log = desc[0].text
                    app_desc = desc[1].text

                if (len(record_list.find_all(class_="screenshot-box")) > 0):
                    # print(record_list.find_all(class_="screenshot-box"))
                    app_imgs = record_list.find_all(class_="screenshot-box")[0].find_all("img")
                    print(app_imgs)
                    for app_img in app_imgs:
                        # print(1)
                        # app_imgurl = app_imgurl + app_img.get("src") + '\n'
                        app_imgurl = app_imgurl + app_img.get("src")
                        print(app_imgurl)

                app_id = appid
                app_record_value = (
                app_id, app_name, app_subtitle, app_version, app_date, app_log, app_desc, app_imgurl)
                app_data.append(app_record_value)
                app_name, app_subtitle, app_version, app_date, app_log, app_desc, app_imgurl = [""] * 7
                # print("---------------------")

    # print(soup.prettify())
    get_page_data()

    #分页爬取数据
    pages = soup.find_all(class_="page ivu-page")[0].find_all('li')
    page_actives = soup.find_all(class_="ivu-page-item-active")
    page_active = page_actives[0].a.text
    # print(page_active)
    # print(pages[-2].a.text)
    while(page_active != pages[-2].a.text):
        # print(1)
        page_next = browser.find_element_by_class_name("ivu-page-next")
        time.sleep(3)
        browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
        page_next.click()
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        get_page_data()
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        pages = soup.find_all(class_="page ivu-page")[0].find_all('li')
        page_actives = soup.find_all(class_="ivu-page-item-active")
        page_active = page_actives[0].a.text

    browser.close()
    return app_data

print(scrapy_qimai_app_search(1166869299))