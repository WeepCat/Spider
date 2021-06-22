# !/usr/bin/env python
# -*- coding:utf-8 -*-
# outhor:xinlan time:

"""
将爬取的csv文件导入mysql数据库
"""

import pymysql

# 打开数据库连接
conn = pymysql.connect(host='localhost', port=3306, user="root", password="120133", db = "dblab")
# print(conn)
# print(type(conn))

# 获取游标
cursor = conn.cursor()

# 创建pythonDB数据库
cursor.execute('Create database if not exists pythonDB;')

# 创建data表
cursor.execute("create table if not exists data ")
