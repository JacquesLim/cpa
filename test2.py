import requests
from selenium import webdriver
import time
from db import Database
from bs4 import BeautifulSoup
import re

text = b'insert into f_posts(discussion_id, number, created_at, user_id, type, content) values '
with open('D:/BaiduNetdiskDownload/posts.sql', 'rb')as f:
    n = 0
    for line in f:
        with open('D:/BaiduNetdiskDownload/posts_alls.sql', 'ab+')as ff:
            ff.write(text + line)
        n += 1

# text = 'insert into f_discussion_tag(discussion_id, tag_id) values '
# with open('D:/BaiduNetdiskDownload/old_ali_flarm_ids.txt', 'r', encoding='utf8')as f:
#     for line in f:
#         with open('D:/BaiduNetdiskDownload/discussion_tag_0613.sql', 'a+', encoding='utf8')as ff:
#             ff.write(text + '({}, 2);\n'.format(line.strip()))
