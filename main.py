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
    '''
    直接插入ali_flarum数据表
    :param ids:
    :return:
    '''
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

def insert_ali_flarum_sql(ids):
    '''
    输出插入ali_flarum的sql语句
    :param ids:
    :return:
    '''
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
    sql_posts = 'insert ignore into ' + table_posts + str(column_posts) + ' values '
    sql_discussions = 'insert ignore into ' + table_discussions + str(column_discussions) + ' values'
    sql_discussion_tag = 'insert ignore into ' + table_discussion_tag + str(column_discussion_tag) + ' values'
    with open('D:/BaiduNetdiskDownload/posts.sql','w+',encoding='utf8')as f:
        with open('D:/BaiduNetdiskDownload/discussions.sql', 'w+', encoding='utf8')as ff:
            with open('D:/BaiduNetdiskDownload/discussion_tag.sql', 'w+', encoding='utf8')as fff:
                f.write(sql_posts)
                ff.write(sql_discussions)
                fff.write(sql_discussion_tag)
                # print(ids)
                for id in ids:
                    # print(id)
                    value_posts = (id, 1, now, 3, 'comment', text_process.get_flarum_appInfo_post(cpa, id))
                    res = cpa.select_appinfo(id)
                    title = res[2]
                    # print(title)
                    post_id = cpa2.get_posts_last_id()[0] + 1
                    value_discussions = (id, title, 1, 1, 1,now , 3, post_id, now, 3, post_id, 1, title, 0, 1, 0, 0)
                    value_disscussion_tag = (id, 2)
                    f.write(str(value_posts))
                    f.write(',\n')
                    ff.write(str(value_discussions))
                    ff.write(',\n')
                    fff.write(str(value_disscussion_tag))
                    fff.write(',\n')

def insert_aliyun_flarum_posts_sql(ids, name):
    '''
    输出插入ali_flarum的f_posts表sql语句
    :param ids:
    :return:
    '''
    table_posts = '`f_posts`'
    column_posts = '(`discussion_id`, `number`, `created_at`, `user_id`, `type`, `content`)'
    now = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    sql_posts = 'insert ignore into ' + table_posts + str(column_posts) + ' values '
    with open('D:/BaiduNetdiskDownload/{}.sql'.format(name),'w+',encoding='utf8')as f:
        #f.write(sql_posts)
        for id in ids:
            text = text_process.get_flarum_appInfo_post(cpa, id)
            if text=='':
                continue
            value_posts = (id, 1, now, 3, 'comment', text)
            f.write(sql_posts+str(value_posts))
            f.write(';\n')

def insert_aliyun_flarum_discussions_sql(cpa, cpa2, ids, name):
    '''
    输出插入ali_flarum的f_discussions表sql语句
    :param ids:
    :return:
    '''
    table_discussions = '`f_discussions`'
    column_discussions = '(`id`, `title`, `comment_count`, `participant_count`, `post_number_index`, `created_at`, `user_id`, `first_post_id`, `last_posted_at`, `' \
                         'last_posted_user_id`, `last_post_id`, `last_post_number`, `slug`, `is_private`, `is_approved`, `is_locked`, `is_sticky`)'
    # now = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    sql_discussions = 'insert ignore into ' + table_discussions + str(column_discussions) + ' values '
    with open('D:/BaiduNetdiskDownload/{}.sql'.format(name),'w+',encoding='utf8')as f:
        for id in ids:
            res = cpa.select_appinfo(id)
            if not res:
                continue
            title = res[2]
            post_res = cpa2.get_posts_last_post_id(id)
            if not post_res:
                continue
            post_id = post_res[0]
            insert_time = post_res[1].strftime( '%Y-%m-%d %H:%M:%S')
            value_discussions = (id, title, 1, 1, 1, insert_time, 3, post_id, insert_time, 3, post_id, 1, title, 0, 1, 0, 0)
            f.write(sql_discussions + str(value_discussions))
            f.write(';\n')
def insert_aliyun_flarum_discussion_tag_sql(ids, name):
    '''
    生成插入discussion_tag的sql
    :param ids:
    :param name:
    :return:
    '''
    table_discussion_tag = '`f_discussion_tag`'
    column_discussion_tag = '(`discussion_id`, `tag_id`)'
    # now = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    sql_discussion_tag = 'insert ignore into ' + table_discussion_tag + str(column_discussion_tag) + ' values '
    with open('D:/BaiduNetdiskDownload/{}.sql'.format(name), 'w+', encoding='utf8')as f:
        for id in ids:
            value_discussion_tag = (id, 2)
            f.write(sql_discussion_tag + str(value_discussion_tag))
            f.write(';\n')

def insert_mac_flarum(id):
    sql = "INSERT IGNORE INTO mac_flarum.f_posts(`discussion_id`,`number`,`created_at`,`user_id`,`type`,`content`,`edited_at`,`edited_user_id`,`hidden_at`,`hidden_user_id`,`ip_address`,`is_private`,`is_approved`) SELECT `discussion_id`,`number`,`created_at`,`user_id`,`type`,`content`,`edited_at`,`edited_user_id`,`hidden_at`,`hidden_user_id`,`ip_address`,`is_private`,`is_approved` FROM tbf_flarum.f_posts WHERE discussion_id={};" \
          "INSERT IGNORE INTO mac_flarum.f_discussions(`id`,`title`,`comment_count`,`participant_count`,`post_number_index`,`created_at`,`user_id`,`last_posted_at`,`last_posted_user_id`,`last_post_number`,`hidden_at`,`hidden_user_id`,`slug`,`is_private`,`is_approved`,`is_locked`,`is_sticky`)SELECT `id`,`title`,`comment_count`,`participant_count`,`post_number_index`,`created_at`,`user_id`,`last_posted_at`,`last_posted_user_id`,`last_post_number`,`hidden_at`,`hidden_user_id`,`slug`,`is_private`,`is_approved`,`is_locked`,`is_sticky` FROM tbf_flarum.f_discussions WHERE id={};" \
          "INSERT IGNORE INTO mac_flarum.f_discussion_tag(`discussion_id`,`tag_id`) SELECT `discussion_id`,`tag_id` FROM tbf_flarum.f_discussion_tag WHERE discussion_id={};".format(id,id,id)
    return sql
if __name__ == "__main__":
    #数据库字段声明
    host = "rm-wz995s1cl86g21j840o.mysql.rds.aliyuncs.com"
    port = 3306
    user = "flarum"
    passwd = "Linzhiqi123"
    db = "app_ios"
    charset = "utf8"
    cpa = Database(host, port, user, passwd, db, charset)
    db2 = "tbf_flarum"
    cpa2 = Database(host, port, user, passwd, db2, charset)
    db3 = "mac_flarum"
    cpa3 = Database(host, port, user, passwd, db3, charset)


    #with open('D:/BaiduNetdiskDownload/new_ali_flarm_ids.txt', 'r', encoding='utf8')as f:
        #with open('D:/BaiduNetdiskDownload/test_mac_flarum.sql', 'w+', encoding='utf8')as ff:
            #for id in f:
                #sql = insert_mac_flarum(id.strip())
                #ff.write(sql)
                #ff.write('\n')
                #print(sql)
                #cpa3.query_sql(sql)
    # with open('D:/BaiduNetdiskDownload/test_mac_flarum.sql', 'rb')as f:
    #     with open('D:/BaiduNetdiskDownload/test_mac_flarum2.sql', 'wb+')as ff:
    #         for line in f:
    #             ff.write(line)
    #             ff.write(b'commit;\n')


    #生成导入flarum的三个表的sql语句
    with open('D:\BaiduNetdiskDownload\myjob\python\itunes_monitor\datafile\\app_urls_inc\\2019_6_23_22_48\\all_appIds.txt', 'r', encoding='utf8')as f:
        ids = f.read().replace('\ufeff','').strip().split('\n')
        ids = [int(x) for x in ids]
        insert_aliyun_flarum_discussion_tag_sql(ids,'f_discussion_tag_0624')
        # insert_aliyun_flarum_discussions_sql(cpa, cpa2, ids,'f_discussions_0624')
        # insert_aliyun_flarum_posts_sql(ids,'f_posts_0624')



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