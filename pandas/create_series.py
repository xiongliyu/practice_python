#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

"""create series
一维数组. 自动创建索引,也可以自定义创建索引, 自定义索引也可以理解为行的标示
当想series传入一下数据类型时:

list: 将list转化为array, 并且自动创建索引
string: 讲string传入array中成为其唯一元素
dict: 逐个将key作为index, key对应的value,是array中的元素
set: TypeError: 'set' type is unordered
tuple: 将list复制一份转化为array类型, 自动创建索引, 预估成为array之后是可以改变的
number: 将number转化为array,成为该array唯一元素
boolean: 将boolean转化为array,成为该array唯一元素
"""

l = [1, 3, 5, np.nan, 6, 8]
l1 = 'abcd'
l2 = {'a': 1, 'b': True}
l3 = set([1, 2, 3, 4])
l4 = (1, 2, 3, 4)
l5 = 5
l6 = True


s = pd.Series(l5)
print(s)


'''series index
series 需要注意的地方是:
1. index不是再自动判断,所以index数量必须与array的元素数量一致
2. pd.date_range(), 是pandas用来创建日期的, 接受两个参数:1, 开始数据, 2.periods:生成多少个index
3. 我们可以用python的生成器来创建index, 或者直接使用list
4. pd.Series(), 常用参数有3个: 1.data 2.index, 3.dtype

'''
dates = pd.date_range('201001010000', periods=6)
dates1 = [x * x for x in range(9)]
dates2 = [1, 2, 3, 4, 5, 6]

s1 = pd.Series(l, dates1)
print(s1)
