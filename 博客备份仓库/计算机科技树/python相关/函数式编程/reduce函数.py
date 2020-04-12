#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :reduce函数.py
# @Time      :2020/4/12 20:31
# @Author    :亮亮
from functools import reduce

# 求和
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x, y):
    return x + y


def main():
    it = reduce(f, a)
    print(it)


if __name__ == '__main__':
    main()
