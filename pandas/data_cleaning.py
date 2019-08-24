#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame

index = ['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei']
columns = ['English', 'Math', 'Chinese']
data = [
    [65, 30, 66],
    [85, 98, 95],
    [92, 96, 93],
    [88, 77, 90],
    [90, 90, 80]
]
data1 = {
    'Chinese': [66, 95, 93, 90, 80],
    'English': [65, 85, 92, 88, 90],
    'Math': [30, 98, 96, 77, 90]
}
df1 = DataFrame(data1)
df2 = DataFrame(data=data, index=index, columns=columns)
csv_path = r'/home/root-xly/Desktop/my_project/practice_python/pandas/csv/test.csv'
df2.to_csv(csv_path)
