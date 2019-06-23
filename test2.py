import requests
from selenium import webdriver
import time
# from db import Database
from bs4 import BeautifulSoup
import re

# text = b'insert into f_posts(discussion_id, number, created_at, user_id, type, content) values '
# with open('D:/BaiduNetdiskDownload/pusts_full/posts_full_2.sql', 'rb')as f:
#     n = 0
#     for line in f:
#         with open('D:/BaiduNetdiskDownload/pusts_full/posts_n_-{}.sql'.format(n%20), 'ab+')as ff:
#             ff.write(line)
#         n += 1

# with open('D:/BaiduNetdiskDownload/posts_full.sql', 'r', encoding='utf8')as f:
#     with open('D:/BaiduNetdiskDownload/posts_full_2.sql', 'a+', encoding='utf8')as ff:
#         for line in f:
#             ff.write(line.replace('insert into', 'insert ignore into'))

# text = 'insert into f_discussion_tag(discussion_id, tag_id) values '
# with open('D:/BaiduNetdiskDownload/new_ali_flarm_ids_1.txt', 'r', encoding='utf8')as f:
#     for line in f:
#         with open('D:/BaiduNetdiskDownload/discussion_tag_0618_1.sql', 'a+', encoding='utf8')as ff:
#             ff.write(text + '({}, 2);\n'.format(line.strip()))

# with open('D:/BaiduNetdiskDownload/posts_full_2.sql', 'rb')as f:
#     with open('D:/BaiduNetdiskDownload/discussions_0615.sql', 'rb')as ff:
#         with open('D:/BaiduNetdiskDownload/discussion_tag_0615.sql', 'rb')as fff:
#             with open('D:/BaiduNetdiskDownload/post_discussion_tag_0615.sql', 'wb+')as ffff:
#                 line1 = f.readline()
#                 line2 = ff.readline()
#                 line3 = fff.readline()
#
#                 while line1:
#                     ffff.write(b'start transaction;')
#                     ffff.write(line1)
#                     ffff.write(line2)
#                     ffff.write(line3)
#                     ffff.write(b'commit;')
#                     line1 = f.readline()
#                     line2 = ff.readline()
#                     line3 = fff.readline()

#生成汉字的itunes查询链接
with open(u'D:/BaiduNetdiskDownload/常用汉字3500.txt', 'r', encoding='utf8')as f:
    hanzi_list = list(f.read())
    # print(hanzi_list)
    with open('D:\BaiduNetdiskDownload\myjob\python\itunes_monitor\datafile\genre_links.txt', 'r', encoding='utf8')as ff:
        with open('D:\BaiduNetdiskDownload\myjob\python\itunes_monitor\datafile\hanzi_links.txt', 'w+', encoding='utf8')as fff:
            for gener in ff:
                for hanzi in hanzi_list:
                    fff.write(gener.strip())
                    fff.write('?letter={}'.format(hanzi))
                    fff.write('\n')
