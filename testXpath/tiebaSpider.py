# coding:utf8

from multiprocessing.dummy import Pool as ThreadPool
from lxml import etree
import requests
import json

# 为了输出的编码是中文
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def towrite(contentdict):
    f.writelines(u'回帖时间:' + str(contentdict['topic_reply_time']) + '\n')
    f.writelines(u'回帖内容:' + str(contentdict['topic_reply_content']) + '\n')
    f.writelines(u'回帖人:' + str(contentdict['user_name']) + '\n')


def spider(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot', ''))
        author = reply_info['author']['user_name']
        reply_time = reply_info['content']['date']
        content = each.xpath(
            'div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')
        item['user_name'] = author
        item['topic_reply_content'] = content[0]
        item['topic_reply_time'] = reply_time
        towrite(item)


# 测试方法
def test():
    url = "http://tieba.baidu.com/p/3522395718?pn=1"
    html = requests.get(url).text

    # // *[ @ id = "j_p_postlist"] / div[2]
    # // *[ @ id = "j_p_postlist"] / div[1]
    selector = etree.HTML(html)
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    print content_field

    for each in content_field:
        data = each.xpath('@data-field')[0].replace('&quot', '')
        reply_info = json.loads(data)
        author = reply_info['author']['user_name']
        print author
        # // *[ @ id = "post_content_62866840315"]
        content = each.xpath(
            'div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')
        print content

        # print data

        # print html


def test2():
    html = requests.get("http://tieba.baidu.com/p/3522395718?pn=1")
    selector = etree.HTML(html.text)
    content_field = selector.xpath('//div[@class="l_post j_l_post l_post_bright  "]')
    item = {}
    for each in content_field:
        reply_info = json.loads(each.xpath('@data-field')[0].replace('&quot', ''))
        author = reply_info['author']['user_name']
        reply_time = reply_info['content']['date']
        content = each.xpath(
            'div[@class="d_post_content_main"]/div/cc/div[@class="d_post_content j_d_post_content  clearfix"]/text()')
        item['user_name'] = author
        item['topic_reply_content'] = content
        item['topic_reply_time'] = reply_time
        content2 = content[0].replace(' ', '')
        print content[0]
        print content2


if __name__ == '__main__':
    # test()
    # test2()

    pool = ThreadPool(8)
    f = open('content.txt', 'a')
    page = []
    for i in range(1, 21):
        newpage = 'http://tieba.baidu.com/p/3522395718?pn=' + str(i)
        page.append(newpage)

    results = pool.map(spider, page)
    pool.close()
    pool.join()
    f.close()
