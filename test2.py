import requests
from db import Database
from bs4 import BeautifulSoup
import re
from lxml import etree

url = 'https://www.baidu.com/link?url=MNYWCkEd0r4nJicmJbgeZcmXTInjDdDgy-QoLMbVW9eME2qTaNEjVGF8oW6gtDe3CzdB2bq0MuaqU5Xdcowhja&wd=&eqid=976d72b70000b7d3000000065ce657ff'
html = requests.get(url, timeout=10)
print(html.url)