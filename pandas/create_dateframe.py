#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

'''create DataFrame
DataFrame 数据桢,数据表,;类似于excel
特点:
1. 他是Series的集合
2. 与Series的区别: 
    2.1 series吧通过自定义index,当做标记,实现行,一维列表
    2.2 DataFrame通过在'吧自定义index当做标记实现行'上与Series是一致,
    2.3 DataFrame 除了行以外,还提供了columns(列), 每一列都是一个Series,所以DataFrame是Series的集合,通过colums将Series集合在一起
3. DataFrame 支持花式索引, 以及提供API方便我们处理数据
4. 每一个DataFrame(表),内部的数据最好是具有相同columns的数据, 行:往外代表数据的多少,列:往往代表数据的特点和结构
5. DataFrame: 每一行代表着一组完整的数据集,其中每一个数据有自己的属性.每一个columns 应该是一种数据类型,代表这该数据结构的每一个属性或数据类型
'''

# index:datatime_list, columns:list, data:ndarray
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

# 通过dict 创建对象, 且个一个columns数据类型不同, 自动填充数据:
# data:dict_value, index:auto_create_index, columns:dict_key

data1 = {
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(5)), dtype='float32'),
    'D': np.array([3] * 5, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train', 'train']),
    'F': 'foo'
}

df2 = pd.DataFrame(data1)
print(df2)
print(df2.dtypes)