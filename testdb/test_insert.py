# coding:utf8
from __future__ import print_function

import torndb
import json
import simplejson

db = torndb.Connection(
    host='host',
    database='test_db',
    user='user',
    password='password',
    charset='utf8'
)

sql = 'insert into t_student(sid,sname) values(2,"小刚")'

id = db.insert(sql)
print(id)
