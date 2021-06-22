# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:
import time

import requests
"""
参数输入：网页url
函数返回：网页的html信息
"""

def getHtml(url):

    proxies = {
        # "https":"103.85.84.119:25193",
        "https":"42.55.182.221:64256",
        # "https":"114.226.174.211:64256",
    }

    # 设置请求头
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }

    # 请求访问目标url
    resp = requests.get(url, headers=headers)
    # 设置编码格式
    # resp.encoding = encoding

    # 得到html信息
    html = resp.text

    # 关闭远程连接
    resp.close()

    # 防一手锁ip
    time.sleep(2)

    return html

