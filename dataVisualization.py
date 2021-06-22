# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

import matplotlib.pyplot as plt
from pyecharts.charts import Bar
import pandas as pd

file = "data/预处理后数据.csv"
data = pd.read_csv(file, encoding='gbk')

for i in range(len(data)):
    # if "联想" in data['商品名称'].iloc[i] and "Think" not in data['商品名称'].iloc[i]:
    #     print(data['商品名称'].iloc[i])

    if "Think" in data['商品名称'].iloc[i]:
        print(data['商品名称'].iloc[i])
