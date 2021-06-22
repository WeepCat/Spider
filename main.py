# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

import time
from getHtml import getHtml
from getProductInfo import getProductInfo
from getCommentInfo import getCommentInfo
import csv
from concurrent.futures import ThreadPoolExecutor


# 打开csv文件
file = open("data/笔记本电脑数据.csv", "a", encoding='gbk', newline="")
csv_writer = csv.writer(file)

# 设置列索引
csv_writer.writerow(["商品名称", "商品价格", "评论总数", "好评率", "评论热词", "商品id"])
# csv_writer.writerow(["商品名称", "商品价格", "评论总数", "好评率", "商品id"])

def getData(page):
    # 远程访问，并获取html信息
    url = f"https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&pvid=fca40adbb36040f199b620e280391255&page={page}"
    html = getHtml(url)

    # 使用xpath解析,获取商品信息
    prices, names, product_ids = getProductInfo(html)

    # 通过product_id找到商品的评论信息
    for i in range(0, len(product_ids)):

        key_words, total_comment, good_rate = getCommentInfo(product_ids[i])
        # total_comment, good_rate = getCommentInfo(product_ids[i])

        # 返回并输出商品信息
        csv_writer.writerow([names[i], prices[i], total_comment, good_rate, key_words, product_ids[i]])
        # print("finish")
        # csv_writer.writerow([names[i], prices[i], total_comment, good_rate, product_ids[i]])

    print("第" + str(page) + "页" + "采集完成")

    # 防一手锁ip
    time.sleep(20)


if __name__ == '__main__':

    # 创建线程池
    with ThreadPoolExecutor(3) as t:
        for page in range(1,51):
            t.submit(getData(page))

    print("finished")

# https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&pvid=4b71a4fdb16e492cad37fab8af6f614c&page=1&s=116&click=0
# https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&pvid=4b71a4fdb16e492cad37fab8af6f614c&page=3&s=56&click=0
# https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&pvid=4b71a4fdb16e492cad37fab8af6f614c&page=5&s=116&click=0