import requests
from selenium import webdriver
import time
from db import Database
from bs4 import BeautifulSoup
import re
# from lxml import etree
def get_appid(url):
    com = re.compile('id(\d+)?')
    id = com.findall(url)[0]
    return id
driver_url = r"/usr/local/bin/chromedriver"
# url = 'https://music.163.com/#/playlist?id=441009203&userid=317219758'
url = 'https://music.163.com/#/playlist?id=35968825&userid=317219758'

# options = webdriver.ChromeOptions()
# browser = webdriver.Chrome(executable_path=driver_url, chrome_options=options)
# browser.get(url)
# time.sleep(3)
html = requests.get(url, timeout=10)
time.sleep(5)
# print(html.text)
# soup = BeautifulSoup(browser.page_source, 'html.parser')
# ids = soup.find_all('id=(\d+)?')
com = re.compile('id=(\d+)?')
ids = com.findall(html.text)
ids = {'http://music.163.com/song/media/outer/url?id={}.mp3'.format(x) for x in ids}
# print(ids)
with open('/Users/Jacques/Downloads/music163/url.txt','a+',encoding='utf8')as f:
    for u in ids:
        f.write(u)
        f.write('\n')
