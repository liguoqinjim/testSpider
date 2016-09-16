# coding:utf8
from lxml import etree

html1 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
</body>
</html>
'''

html2 = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div id="test3">
        上北，
        <span id="right">
            左西，
            <ul>中-
                <li>发白，</li>
            </ul>
            右东，
        </span>
        下南。
    </div>
</body>
</html>
'''

#starts-with
selector = etree.HTML(html1)
content = selector.xpath('//div[starts-with(@id,"test")]/text()')
for each in content:
    print each


#string(.)
selector2 = etree.HTML(html2)

#不用string(.)
print '不用string(.)'
content2 = selector2.xpath('//div[@id="test3"]/text()')
for each in content2:
    print each

#使用string(.)
print '使用string()'
data = selector2.xpath('//div[@id="test3"]')[0]
info = data.xpath('string(.)')
print info
content3 = info.replace('\n','').replace(' ','')
print content3
