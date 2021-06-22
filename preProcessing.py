# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

import pandas as pd


file = "data/笔记本电脑数据.csv"
data = pd.read_csv(file, encoding="gbk")
# print(data)
data = data.drop_duplicates()
# print(data)

chars = "[' ']"

for i in range(len(data)):

    # 处理商品名称
    data['商品名称'].iloc[i] = data['商品名称'].iloc[i].replace("['", "").replace("']", "").replace("', '", "").replace("', ' ", "").replace("\\t","").replace("\\n", "")

    # 处理商品价格
    data['商品价格'].iloc[i] = float(data['商品价格'].iloc[i].replace("['", "").replace("']", ""))

    # 处理评论热词
    for c in chars:
        data['评论热词'].iloc[i] = data['评论热词'].iloc[i].replace(c, "")

data.to_csv('./data/预处理后数据.csv', index=0, encoding='gbk')