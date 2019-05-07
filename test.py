from bs4 import BeautifulSoup
import requests
import random
import base64


def base_code(username, password):
    str = '%s:%s' % (username, password)
    encodestr = base64.b64encode(str.encode('utf-8'))
    return '%s' % encodestr.decode()

url = "http://myip.ipip.net/"
username = '18565754151'
password = 'Zhiqi123'
basic_pwd = base_code(username, password)

# proxy_ip_api = r'http://api.wandoudl.com/api/ip?app_key=a0be971e2890002cf2c0131a1ccb6406&pack=0&num=20&xy=2&type=1&lb=\n&mr=2&'
proxy_ips = [
    '220.178.193.203:23564',
    '221.203.95.67:36410',
    '60.179.236.247:766',
    '223.241.176.60:3617',
    '182.240.197.232:36410',
    '220.164.232.109:894',
    '222.220.154.178:23564',
    '117.93.177.2:23564',
    '114.226.92.53:36410',
    '175.44.157.78:766',
    '114.228.202.153:3617',
    '183.2.100.253:3617',
    '106.92.102.254:5412',
    '101.205.44.137:766',
    '61.137.153.221:894',
    '182.247.36.169:23564',
    '115.151.247.213:36410',
    '175.160.147.131:766',
    '60.185.65.152:5412',
    '182.101.203.122:766'
]
ip = random.choice(proxy_ips)
print(proxy_ips)
headers = {
    'Proxy-Authorization': 'Basic %s' % (base_code(username, password))
}

proxy = {
    'http' : 'socks5://{}'.format(ip),
    'https' : 'socks5://{}'.format(ip)
}

r = requests.get(url,proxies=proxy, headers=headers)
print(r.text)