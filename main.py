from db import Database
import text_process
import datetime,json,time
# import scrapy
# import app

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

def insert_ali_flarum(ids):
    table_posts = 'f_posts'
    table_discussions = 'f_discussions'
    table_discussion_tag = 'f_discussion_tag'
    column_posts = '(discussion_id, number, created_at, user_id, type, content)'
    column_discussions = '(id, title, comment_count, participant_count, post_number_index, created_at, user_id, first_post_id, last_posted_at, ' \
                         'last_posted_user_id, last_post_id, last_post_number, slug, is_private, is_approved, is_locked, is_sticky)'
    column_discussion_tag = '(discussion_id, tag_id)'
    datatype_posts = "(%s, %s, str_to_date(%s,'%%Y-%%m-%%d %%H:%%i:%%s'), %s, %s, %s)"
    datatype_discussions = "(%s, %s, %s, %s, %s, str_to_date(%s,'%%Y-%%m-%%d %%H:%%i:%%s'), %s, %s, str_to_date(%s,'%%Y-%%m-%%d %%H:%%i:%%s'), " \
                           "%s, %s, %s, %s, %s, %s, %s, %s)"
    datatype_discussion_tag = "(%s, %s)"
    now = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    # now = datetime.datetime.fromtimestamp(time.mktime(time.strptime(now, ('%Y-%m-%d %H:%M:%S'))))
    # print(now)
    # print(type(now))
    values_posts = []
    values_discussions = []
    values_disscussion_tag = []

    for id in ids:
        value_posts = (id, 1, now, 3, 'comment', text_process.get_flarum_appInfo_post(cpa, id))
        res = cpa.select_appinfo(id)
        title = res[2]
        # print(title)
        post_id = cpa2.get_posts_last_id()[0] + 1
        value_discussions = (id, title, 1, 1, 1, now, 3, post_id, now, 3, post_id, 1, title, 0, 1, 0, 0)
        value_disscussion_tag = (id, 2)
        values_posts.append(value_posts)
        values_discussions.append(value_discussions)
        values_disscussion_tag.append(value_disscussion_tag)
        # print(datatype)

    # print(values_posts)
    cpa2.insert(table_posts, column_posts, datatype_posts, values_posts)
    cpa2.insert(table_discussions, column_discussions, datatype_discussions, values_discussions)
    cpa2.insert(table_discussion_tag, column_discussion_tag, datatype_discussion_tag, values_disscussion_tag)

if __name__ == "__main__":
    #数据库字段声明
    host = "rm-wz9rw2pr9mox4w6m1go.mysql.rds.aliyuncs.com"
    port = 3306
    user = "root"
    passwd = "Root@2017"
    db = "app_ios"
    charset = "utf8"
    cpa = Database(host, port, user, passwd, db, charset)
    db2 = "ali_flarum"
    cpa2 = Database(host, port, user, passwd, db2, charset)

    with open('/Users/Jacques/Downloads/ids.txt','r',encoding='utf8')as f:
        # ids = f.read().strip().split('\n')
        for line in f:
            ids = [int(line.strip())]
            insert_ali_flarum(ids)
            # print(ids)
    # ids = [284145181]
    # ids = [281736535]
    # print(text_process.get_flarum_appInfo_post(cpa, 284943962))




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
    # appinfo_db = cpa.select_all_app()
    # for app_info in appinfo_db:
    #     # print(app_info[0])
    #     latest_db = cpa.select_latest_record_date(app_info[0])
    #     appinfo_page = scrapy.scrapy_qimai_app_search(app_info[0],1)
    #     if(len(appinfo_page)>3):
    #         latest_page = appinfo_page[3][4]
    #         print(latest_db)
    #         print(latest_page)
    #         if(latest_db!=latest_page):
    #             insert_appid_record(app_info[0])

    # app.get_all_appid('C:/Users/mayn/Desktop/appid.txt', 'C:/Users/mayn/Desktop/done.txt', ['6018'], 'E', 53)
    # print(app.get_proxy_ip())
    # print(app.get_proxy())