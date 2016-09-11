# coding:utf8

import requests
from lxml import etree

url = "http://weibo.cn/u/1890493665"
url_login = "https://login.weibo.cn/login/"

html = requests.get(url).content
selector = etree.HTML(html)
password = selector.xpath('//input[@type="password"]/@name')[0]
vk = selector.xpath('//input[@name="vk"]/@value')[0]
action = selector.xpath('//form[@method="post"]/@action')[0]
print password
print action
print vk
new_url = url_login + action
data = {
    'mobile' : '用户名',
    password : '密码',
    'remember' : 'on',
    'backURL' : 'http://weibo.cn/u/1890493665',
    'backTitle' : u'微博',
    'tryCount' : '',
    'vk' : vk,
    'submit' : u'登录'
}
newhtml = requests.post(new_url,data=data).content
#由于现在weibo.cn修改为登录的时候会需要图片验证码，所以这个现在这个方式登录无效了。但是使用post来模拟登录的方法还是一样的
print newhtml