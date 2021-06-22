# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

"""
参数输入：网页的html信息
函数返回：商品价格、商品名称、商品id
"""

from lxml import etree

def getProductInfo(html):

    # xpath解析
    html = etree.HTML(html)

    # 拿到每一个商品的div
    divs = html.xpath('//*[@id="J_goodsList"]/ul/li')
    # //*[@id="J_goodsList"]/ul/li[1]/div/div[2]/strong/i
    # //*[@id="J_goodsList"]/ul/li[1]/div/div[3]/a/em/font

    # 保存网页中所有商品的信息
    prices = []
    names = []
    product_ids = []

    for div in divs:
        # 商品价格
        price = div.xpath("./div/div[2]/strong/i/text()")
        prices.append(price)
        # 商品名称
        name = div.xpath("./div/div[3]/a/em//text()")
        names.append(name)
        # 商品id
        # //*[@id="J_comment_100009087897"]
        product_id = div.xpath('.//div[@class="p-commit"]/strong/a/@id')[0].replace("J_comment_", "")
        product_ids.append(product_id)

    # 调试
    # print(len(product_ids))

    return prices, names, product_ids
