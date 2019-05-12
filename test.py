# smilar = 'https://itunes.apple.com/cn/app/app/id1335458066#see-all/customers-also-bought-apps'
# download = 'https://itunes.apple.com/lookup?id={1191692521,1335458066}&country=cn&entity=software'
from bs4 import BeautifulSoup
import requests
headers = {
      'X-Apple-Store-Front': '143465,12'

    }
html = requests.get('https://itunes.apple.com/cn/customer-reviews/id1335458066?displayable-kind=11', headers)
print(html.text)
