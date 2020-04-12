#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :filter_1.py
# @Time      :2020/4/12 20:53
# @Author    :亮亮
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fun(x):
    return x % 2 == 1


def main():
    it = filter(fun, a)  # it是一个可迭代对象
    print(list(it))


if __name__ == '__main__':
    main()

"""
[1, 3, 5, 7, 9]
"""