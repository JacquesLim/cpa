from db import Database
import scrapy

def insert_appid_record(appid):
    #搜索APPID，并插入数据库
    dataset2 = scrapy.scrapy_qimai_app_search(appid)
    table2 = dataset2[0]
    column2 = dataset2[1]
    datatype2 = dataset2[2]
    value2 = dataset2[3:]
    print(table2)
    print(column2)
    print(datatype2)
    print(value2)
    cpa.insert(table2, column2, datatype2, value2)

if __name__ == "__main__":
    #数据库字段声明
    host = "rm-wz9rw2pr9mox4w6m1go.mysql.rds.aliyuncs.com"
    port = 3306
    user = "root"
    passwd = "Root@2017"
    db = "cpa"
    charset = "utf8"
    cpa = Database(host, port, user, passwd, db, charset)

    # 搜索关键词，并插入数据库
    # dataset = scrapy.scrapy_qimai_search("中标")
    # table = dataset[0]
    # column = dataset[1]
    # datatype = dataset[2]
    # value = dataset[3:]
    # print(table)
    # print(column)
    # print(datatype)
    # print(value)
    # cpa.insert(table, column, datatype, value)

    #爬取所有APPID的最新迭代记录
    appinfo_db = cpa.select_all_app()
    for app_info in appinfo_db:
        # print(app_info[0])
        latest_db = cpa.select_latest_record_date(app_info[0])
        appinfo_page = scrapy.scrapy_qimai_app_search(app_info[0],1)
        if(len(appinfo_page)>3):
            latest_page = appinfo_page[3][0]
            if(latest_db!=latest_page):
                insert_appid_record(app_info[0])

