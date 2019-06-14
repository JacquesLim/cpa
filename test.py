# smilar = 'https://itunes.apple.com/cn/app/app/id1335458066#see-all/customers-also-bought-apps'
# download = 'https://itunes.apple.com/lookup?id={1191692521,1335458066}&country=cn&entity=software'
# rasting = 'https://itunes.apple.com/cn/customer-reviews/id1335458066?displayable-kind=11'
from bs4 import BeautifulSoup
import requests
from readability import Document
from aip import AipNlp

# """ 你的 APPID AK SK """
# APP_ID = '15827943'
# API_KEY = 'eOkQjloKyEGX77h5EtIpKyNg'
# SECRET_KEY = 'v73VmZGG7tc7UnnS9I32IdlUh518Nh8Y'
#
# client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
# text = "How damaging is the Huawei row for the US and China?"
#
# """ 调用词法分析 """
# print(client.lexer(text))

# with open('C:/Users/mayn/Desktop/test.html','rb')as f:
#     html = f.read()
response = requests.get('https://www.bbc.com/news/technology')
doc = Document(response.text)
print(doc.title())
print(doc.summary())