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

sql = 'select * from t_student'
rows = db.query(sql)
for row in rows:
    print(json.dumps(row, ensure_ascii=False))

