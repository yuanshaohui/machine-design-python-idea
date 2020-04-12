#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :resuce_2.py
# @Time      :2020/4/12 20:43
# @Author    :亮亮
from functools import reduce
# 将列表中的每个数字拼成一个整数
a = [1, 2, 3, 4]


def f(x, y):
    return x*10+y


def main():
    it = reduce(f, a)
    print(it)


if __name__ == '__main__':
    main()

"""
1234
"""