#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)


'''view data
df.head(): 从头部开始查看数据. 接受一个参数(number), 表示查看多少条数据
df.tail(): 从尾部开始查看数据. 接受一个参数(number), 表示查看多少条数据
df.index: 查看该数据集的index, 返回一个columns_list
df.columns: 查看数据集columns,返回一个columns_list
df.to_numpy(): 将DataFrame转化为numpy的ndarray
df.describe(): 提供DateFrame摘要
df.T: 转置数据(将index与columns对换)
df.sort_values(by= ): 按值排序,by的值是其中一个columns
'''

# print(df.head(3))
# print(df.tail(2))

# print()
print(len(df.index))
print(len(df.columns))
# print()
print(df.columns[1])
print(df.index[0])
print([x for x in df.columns])
print([x for x in df.index])

'''DataFrame转换为ndarray
DataFrame_to_numpy() 将DataFrame装换为Numpy对象(ndarray)
与numpy区别: numpy 数据类型相同,而pandas每一列都可以是一种数据类型
pandas 在转换为numpy时,会去numpy找符合DataFrame的数据类型.或者将数据强制转化为python对象,所以转化为numpy时,数据类型为object
pandas转化为numpy时:
1. 没有了index/columns,所有的数据转化为2维数组
2. DataFrame的每一行都是一个子数组
'''

# 浮点数转化为numpy, 特点:高效
print(df)
print(df.to_numpy())



# 显示数据并快速统计摘要
print(df.describe())

# 转置数据(将index与columns对换)
print(df.T)

# 按值排序
print(df.sort_values(by='B'))