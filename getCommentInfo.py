# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

"""
参数输入：商品id
函数输出：返回商品的评论信息：评论总数、好评率、评论关键字
"""

import json
from getHtml import getHtml

def getCommentInfo(product_id):

    # 设置url
    url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={product_id}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    # url = f"https://club.jd.com/comment/productCommentSummaries.action?referenceIds={product_id}&callback=jQuery8827474&_=1615298058081"
    # https: // club.jd.com / comment / productCommentSummaries.action?referenceIds = 100016777664 & callback = jQuery1106317 & _ = 1624254853417    # 得到网页html信息
    # https: // club.jd.com / comment / productCommentSummaries.action?referenceIds = 100016777664 & callback = jQuery8827474 & _ = 1615298058081
    text = getHtml(url)

    # 替换json头
    # text = text.replace("jQuery8827474(","").replace(");","")
    text = text.replace("fetchJSON_comment98(","").replace(");", "")

    # 载入json文件，方便查找字典信息
    text = json.loads(text)

    # 商品关键字
    key_words = []
    words = text['hotCommentTagStatistics']
    for word in words:
        key_words.append(word['name'])

    # 评论总数
    total_comment = text['productCommentSummary']['commentCountStr'].replace("+", "")
    # total_comment = text['CommentsCount'][0]['CommentCountStr'].replace("+", "")

    # 文字替换
    if "万" in total_comment:
        total_comment = total_comment.replace("万", "")
        total_comment = str(int(total_comment) * 10000)

    # 好评率
    good_rate = text['productCommentSummary']['goodRate']
    # good_rate = text['CommentsCount'][0]['GoodRateShow']

    # 调试
    print(key_words, total_comment, good_rate)
    # print(total_comment, good_rate)

    return key_words, total_comment, good_rate
    # return total_comment, good_rate