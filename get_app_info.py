#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   get_app_info.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/13 11:11   Jacques Lim    1.0         根据提供的ID，生成插入APPINFO 的sql文件
'''
# smilar = 'https://itunes.apple.com/cn/app/app/id1335458066#see-all/customers-also-bought-apps'
# download = 'https://itunes.apple.com/lookup?id={1191692521,1335458066}&country=cn&entity=software'
from bs4 import BeautifulSoup
import requests
import json
from db import Database

# APP链接文件路径
app_links_path = './datafile/all_app_links.txt'
# 插入数据库sql文件
insert_appinfo_sql_path = './datafile/insert_appinfo_{}.sql'
# log文件
get_app_info_log_path = './log/get_app_info.log'

def get_app_info(id):
    url = 'https://itunes.apple.com/lookup?id={}&country=cn&entity=software'
    app = {}
    try:
        html = requests.get(url.format(id), timeout=10)
        app = json.loads(html.text)['results'][0]
        table = 'app_info'
        column = '(id,appId,title,url,description,icon,genres,genreIds,primaryGenre,primaryGenreId,contentRating,languages,size,requiredOsVersion,released,updated,releaseNotes,version,price,currency,free,developerId,developer,developerUrl,developerWebsite,averageUserRating,userRatingCount,currentVersionRating,currentVersionRatingCount,screenshots,ipadScreenshots,appletvScreenshots,supportedDevices)'
        val = [(
            app.setdefault('trackId', ""),
            app.setdefault('bundleId', ""),
            app.setdefault('trackName', ""),
            app.setdefault('trackViewUrl', ""),
            app.setdefault('description', ""),
            app.setdefault('artworkUrl512', "") or app.setdefault('artworkUrl100', "") or app.setdefault('artworkUrl60',
                                                                                                                 ""),
            "{}".format(app.setdefault('genres', "")),
            "{}".format(app.setdefault('genreIds', "")),
            app.setdefault('primaryGenreName', ""),
            app.setdefault('primaryGenreId', ""),
            app.setdefault('contentAdvisoryRating', ""),
            "{}".format(app.setdefault('languageCodesISO2A', "")),
            app.setdefault('fileSizeBytes', ""),
            app.setdefault('minimumOsVersion', ""),
            app.setdefault('releaseDate', ""),
            app.setdefault('currentVersionReleaseDate', "") or app.setdefault('releaseDate', ""),
            app.setdefault('releaseNotes', ""),
            app.setdefault('version', ""),
            app.setdefault('price', ""),
            app.setdefault('currency', ""),
            app.setdefault('price', "") == 0,
            app.setdefault('artistId', ""),
            app.setdefault('artistName', ""),
            app.setdefault('artistViewUrl', ""),
            app.setdefault('sellerUrl', ""),
            app.setdefault('averageUserRating', ""),
            app.setdefault('userRatingCount', ""),
            app.setdefault('averageUserRatingForCurrentVersion', ""),
            app.setdefault('userRatingCountForCurrentVersion', ""),
            "{}".format(app.setdefault('screenshotUrls', "")),
            "{}".format(app.setdefault('ipadScreenshotUrls', "")),
            "{}".format(app.setdefault('appletvScreenshotUrls', "")),
            "{}".format(app.setdefault('supportedDevices', ""))
        )]
        return Database.insert_sql(table, column, val)
    except:
        print('id：{}：爬取失败'.format(id))
        with open(get_app_info_log_path, 'a+', encoding='utf8')as ff:
            ff.write('id：{}：爬取失败'.format(id))
        return None



if __name__ == "__main__":
    with open(app_links_path, 'r', encoding='utf8')as file:
        n=50000
        for line in file:
            n += 1
            id = line.split('/')[6].replace('id', '').replace('?mt=8', '')
            with open(insert_appinfo_sql_path.format(int(n/10000)), 'a+', encoding='utf8')as ff:
                sql = get_app_info(int(id))
                if sql is not None:
                    ff.write(sql)
            if n%1000 ==0:
                print('正在生成第{}行sql'.format(n))

