#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

print(df.iloc[3])