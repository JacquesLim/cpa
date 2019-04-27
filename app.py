from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
res = requests.get('https://www.qimai.cn/')
res.encoding = 'utf-8'
print(res.text)

# html = urlopen("https://www.qimai.cn/").read()
# print(html)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.prettify())
# apps = soup.select("p[class='product-title']")
# print(apps)
# for app in apps:
    # print(app.get_text())
#
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# html = urlopen(u"https://www.qimai.cn/search/index/country/cn/search/??").read().decode('utf-8')
# soup = BeautifulSoup(html, "html.parser")
# titles = soup.select("span[class='word num']")
# for title in titles:
#     print(title.get_text())
