#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import pandas as pd
'''get
requests.get('url', auth)
auth 是对方规定的必须是这个字段
将res.json()转换为Dataframe, key 会转化成columns
'''
r = requests.get('http://api.github.com/user', auth=('xiongliyu', 'tryzgy11'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
# print(r.text)
# print(r.json())
# data = r.json()
# df = pd.DataFrame(data)
# print(df)
# df.to_csv('/home/root-xly/Desktop/my_project/practice_python/pandas/csv/test_github.csv')
