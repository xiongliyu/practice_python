#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

'''获取DataFrame里面元素的几种方式
df['columns_name']: 获取一列数据, 该列数据就是一个Series类型

df[start_index : end_index]: 获取多少行数据, 从start_index开始的行,到end_index行(如果是索引不包含end_index, 自定义是包含的)
注: start_index/end_index: 可以是index, 也可以是行标签

'''

# 获取某一列
print(df['A'])


# 获取某几行
print(df[0:1])
print(df['20190101': '20190102'])


'''通过标签获取
df.loc[index] : 通过index获取某一行(含自定义标签)

df.loc[:, ['columnsA', ...]] : 获取某一列,或者多列

总结: df.loc[行, 列]: 其中行是切片,列是list内部标签
'''

# 获取某一行
print(df.loc[dates[0]])
print(df.loc['20190102'])

# 获取某一列,或某几列
print(df.loc[:, ['A']])
print(df.loc[:, ['A', 'B']])


# 行列两个轴同时切片
print(df.loc['20190101':'20190103', ['A', 'C']])

print(df.loc['20190103', ['A', 'C']])


# 获取标量值(获取某一个值)
print(df.loc[dates[0], 'A'])
print(df.loc['20190101', 'A'])