#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4), index=pd.date_range('20190101', periods=6), columns=list('ABCD'))
s = pd.Series([1, 2, 3, 4, 5, 6, 7], index=pd.date_range('20190101', periods=7))

# 通过创建一个Series, 可以将Series 添加到DataFrame, 这就以为着该表的每一组数据都添加了一个字段
df['F'] = s
print(s)
print(df)


# 通过标签赋值
df.at['20190101', 'A'] = 0
print(df)


# 通过位置赋值 0 1代表行列索引
df.iat[0, 1] = 1
print(df)

# 通过numpy 数组进行赋值/ 赋值通过标签

df.loc[:, 'D'] = np.array([5] * len(df))
df.loc[:, 'C'] = [1, 2, 3, 4, 5, 9]
df.loc['20190101', :] = [1, 1, 1, 1, 1]
print(df)

