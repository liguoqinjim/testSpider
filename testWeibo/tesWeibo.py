# coding:utf8

import requests
from lxml import etree
from multiprocessing.dummy import Pool

# print '不使用cookie来拉取，服务器会自动跳转到登录界面'
# url = "http://weibo.cn/u/1890493665"
# html = requests.get(url).content
# print html

print '使用cookie来登录'
url = "http://weibo.cn/u/1890493665"

cookie = {
    "Cookie": " _T_WM=3f0e8ff5ebab162f5131d1a89075b6ee; ALF=1476195818; SCF=AmC0GlFYTODCRJLHjsUYPLFkEwsL8hnPL19CR5-1UUIgrd94EMIkeSB5LG7wHK5UVy5vxPFiN0d6mqtiRfaPiwQ.; SUHB=0IIlyIx-4tn5yW; SUB=_2A2560RipDeTxGeNI4lsU9CliguorEyDiIHXVWPbjhrDV6PUJbktBeLW_RkW1WXlVXgzfgBjCOTDBHNk-gJYIN6A..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWpuEKiUVVcFsGgwUyqlHLY5JpX5o2p5NHD95QfSo.4SKBX1heXWs4Dqcjci--fiKLFiKL8i--fi-isiKnci--Xi-zRiK.0i--NiK.Xi-2Ri--Ni-i8i-i2i--Ni-iFiK.E"}
html = requests.get(url, cookies=cookie).content
print html

# 这里是为了测试，有一个现象在运行的时候会发生，就是要是开着fiddler再运行爬虫的话，返回的会很慢。把fiddler关了就可以了
# html = requests.get("http://www.baidu.com").content
# print html
