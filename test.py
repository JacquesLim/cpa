# smilar = 'https://itunes.apple.com/cn/app/app/id1335458066#see-all/customers-also-bought-apps'
# download = 'https://itunes.apple.com/lookup?id={1191692521,1335458066}&country=cn&entity=software'
# rasting = 'https://itunes.apple.com/cn/customer-reviews/id1335458066?displayable-kind=11'
from bs4 import BeautifulSoup
import requests
import json
from db import Database
from bs4 import BeautifulSoup
import re

id = 1335458066
url = 'https://itunes.apple.com/cn/app/app/id{}'
html = requests.get(url.format(id), timeout=10)
soup = BeautifulSoup(html.text, 'html.parser')
str = soup.find(id='shoebox-ember-data-store').text
index = str.find('customersAlsoBoughtApps')
com = re.compile(r'"(\d+)"') #匹配“id”
similar = com.findall(str[index:index+700])
similar = [ int(x) for x in similar ] #字符串转数字
print(similar)

table = 'app_info'
field = "similar='{}'".format(similar)
condition = 'id={}'.format(id)
print(Database.update_sql(table, field, condition))
