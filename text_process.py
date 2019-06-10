#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   text_process.py    
@Contact :   258770530@qq.com.com
@Modify Time      @Author        @Version    @Desciption
------------      -------        --------    -----------
2019/5/11 13:05   Jacques Lim    1.0         处理各种文本
'''
import re

'''
配置文件路径
all_appid_path_test: 存储所有APPID
all_app_links_path: 存储所有APP的链接url
'''
all_appid_path_test = './datafile/app_lookup_url.txt'
all_app_links_path_test =  'C:/Users/mayn/Desktop/all_app_links.txt'
genre_letter_pav_links_path = 'C:/Users/mayn/Desktop/genre_letter_pav_links.txt'


def get_lookup_url(text):
    url = "https://itunes.apple.com/lookup?id={}&country=cn&entity=software"
    return url.format(text.split('/')[6].replace('id', '').replace('?mt=8', '').replace('\n',''))

def get_appid(url):
    com = re.compile('id(\d+)?')
    id = com.findall(url)[0]
    return id

def get_last_url(urls, generId, letter):
    s = 'id{}?mt=8&letter={}&page='.format(generId, letter)
    generId_letter_list = []
    for url in urls:
        if s in url:
            generId_letter_list.append('{}-{}:{}'.format(generId, letter, url))
    if len(generId_letter_list)>0:
        return generId_letter_list[-1]
    else:
        return []

def get_genreId(text):
    '''
    这里需要重新处理
    :param text:
    :return:
    '''
    com = re.compile(r'id(\d+)\?')
    all_list = com.findall(text)
    generId_list = list(set(all_list))
    print(generId_list)
    return generId_list

def get_icon_link(url, size):
    '''
    将APP IOS里的图片转换大小，返回链接
    :param url:
    :param size:
    :return:
    '''
    link = url.split('/')
    link[-1] = '{}x{}bb.jpg'.format(size,size)
    url = '/'.join(link)
    return url

def get_text_tran(text):
    '''
    将文本的回车转换为<br/>
    :param text:
    :return:
    '''
    return text.replace('\n', '<br/>\n')

def get_flarum_appInfo_post(cpa, id):
    '''
    生成发布flarum的appinfo代码
    :param id: APP ID
    :return: 一串代码
    '''
    res = cpa.select_appinfo(id)
    txt = ''

    icon = get_icon_link(res[1], 100)
    txt += '<r><p><IMG src="{}"></IMG></p>'.format(icon)

    title = res[2]
    subtitle = str(res[3] or '暂无')
    version = str(res[4] or '暂无')
    # now = (datetime.datetime.now() - datetime.timedelta(hours = 8)).strftime('%Y-%m-%d %H:%M:%S')
    updated = res[5].replace('T', ' ').replace('Z', '')

    developer = str(res[6] or '暂无')
    price = res[7]
    currentVersionRating = res[8]
    currentVersionRatingCount = res[9]
    txt += '<H3><s>### </s><STRONG><s>**</s><e>**</e></STRONG>{}</H3>\n' \
           '<p><STRONG><s>**</s>副标题：<e>**</e></STRONG>{}<br/>\n' \
           '<STRONG><s>**</s>版本号：<e>**</e></STRONG>{}<br/>\n' \
           '<STRONG><s>**</s>发布时间：<e>**</e></STRONG>{}<br/>\n' \
           '<STRONG><s>**</s>开发商：<e>**</e></STRONG>{}<br/>\n' \
           '<STRONG><s>**</s>价格：<e>**</e></STRONG>￥{}<br/>\n' \
           '<STRONG><s>**</s>当前版本评分：<e>**</e></STRONG>{}<br/>\n' \
           '<STRONG><s>**</s>当前评论人数：<e>**</e></STRONG>{}<br/>\n'.format(title, subtitle, version, updated, developer,
                                                                        price, currentVersionRating,
                                                                        currentVersionRatingCount)

    txt += '<STRONG><s>**</s>APP截图：<e>**</e></STRONG><br/>\n'
    screenshots = str(res[10] or '')
    if screenshots != '':
        screenshots = screenshots.replace('[', '').replace(']', '').replace("'", '').split(',')
    else:
        txt += '暂无\n'
    for screenshot in screenshots:
        screenshot = get_icon_link(screenshot, 300)
        ttt = '<IMG src="{}"></IMG>'.format(screenshot)
        txt += ttt
    txt += '<br/>\n'
    releaseNotes = str(res[11] or '暂无')
    releaseNotes = '<STRONG><s>**</s>版本更新说明：<e>**</e></STRONG><br/>\n' + get_text_tran(
        releaseNotes) + '</br>\n'
    txt += releaseNotes + '<br/>\n'

    description = res[12]
    description = '<STRONG><s>**</s>版本描述：<e>**</e></STRONG><br/>\n' + get_text_tran(
        description) + '</br>\n'
    txt += description

    txt += '<p><STRONG><s>**</s>相似APP：<e>**</e></STRONG><br/>\n'
    similar_ids = str(res[13] or '')
    if similar_ids != '':
        similar_ids = similar_ids.split(',')
    else:
        txt += '暂无\n'
    for similar_id in similar_ids:
        similarApp_info = cpa.select_appinfo_smart(similar_id)
        # print(similarApp_info)
        if similarApp_info is not None:
            similar_icon = similarApp_info[1]
            similar_icon = get_icon_link(similar_icon, 100)
            similar_title = similarApp_info[2]
            ttt = '<URL url="/d/{}-{}"><IMG src="{}"></IMG></URL>\n<STRONG><s>**</s><URL url="/d/{}-{}"><s>[</s>{}<e>](/d/{}-{})</e></URL><e>**</e></STRONG><br/>\n'.format(
                similar_id, similar_title, similar_icon, similar_id, similar_title, similar_title, similar_id,
                similar_title)
            txt += ttt
    txt += '</r>'
    return txt

# with open(all_app_links_path_test, 'r', encoding='utf8')as file:
#     n = 0
#     for line in file:
#         n += 1
#         appid = get_appid(line)
#         with open(all_appid_path_test, 'a+', encoding='utf8')as f:
#             f.write(appid + '\n')
#         if n%10000 == 0:
#             print("已处理{}行".format(n))
# letter_list = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
#                 'U', 'V', 'W', 'X', 'Y', 'Z']
# with open(genre_letter_pav_links_path,'r')as f:
#     text = f.read()
#     urls = text.split()
#     generId_list = get_genreId(text)
#     last_url = []
#     for generId in generId_list:
#         for letter in letter_list:
#             last_url.append(get_last_url(urls,generId,letter))
#     print(last_url)

# print(get_appid("https://itunes.apple.com/cn/app/%E9%92%89%E9%92%89/id930368978?mt=8"))