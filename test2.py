#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   test2.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/4/29 15:13   Jacques Lim    1.0         None
'''
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from fake_useragent import UserAgent
ua = UserAgent()
print(ua.chrome)
print(ua.random)
print(ua.random)
print(ua.random)
header = 'user-agent=' + ua.random
options = webdriver.ChromeOptions()
options.add_argument(header)
browser = webdriver.Chrome(chrome_options=options)
wait=WebDriverWait(browser,10)
