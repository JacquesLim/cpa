import time
from selenium import webdriver
from bs4 import BeautifulSoup
driver_url = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

def scrapy_qimai_search(keyword):
    browser = webdriver.Chrome(executable_path=driver_url)
    browser.get("https://www.qimai.cn/search/index/country/cn/search/"+keyword)
    time.sleep(3)
    for i in range(4): #下翻4页，共5页
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
        time.sleep(3)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # print(soup.prettify())
    app_rows = soup.find_all(class_="ivu-table-row")
    # print(apps)
    app_data=[ ("app_id", "app_name", "app_subtitle", "app_publisher", "app_category", "app_category_rank")]
    for app_row in app_rows:
        # app_infos = app_row.select("div[class='info-content'] p")
        app_infos = app_row.find_all(class_="ivu-table-cell")
        # print(len(app_infos))
        if len(app_infos) == 6:
            app_info = app_row.select("div[class='info-content'] p")
            if len(app_info) == 2:
                app_name = app_info[0].a.text
                app_link = app_info[0].a.get('href')
                app_subtitle = ""
                app_publisher = app_info[1].text
            if len(app_info) == 3:
                app_name = app_info[0].a.text
                app_link = app_info[0].a.get('href')
                app_subtitle = app_info[1].text
                app_publisher = app_info[2].text
            app_categoryrank = app_infos[4].find_all('p')
            app_category = app_categoryrank[1].text
            app_category_rank = app_categoryrank[0].text

            app_id = app_link.split('/')[4]
            app_info_value = (app_id, app_name, app_subtitle, app_publisher, app_category, app_category_rank)
            # app_dict={
            #     "app_id": app_id,
            #     "app_name": app_name,
            #     "app_subtitle": app_subtitle,
            #     "app_publisher": app_publisher,
            #     "app_category": app_category,
            #     "app_category_rank": app_category_rank,
            # }
            app_data.append(app_info_value)
            # print(app_name)
            # print(app_id)
            # print(app_subtitle)
            # print(app_publisher)
            # print(app_category)
            # print(app_category_rank)
            # print("-----------------------")
    browser.close()
    return app_data

print(scrapy_qimai_search("投标"))