#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :map应用_多列表传入.py
# @Time      :2020/4/12 20:25
# @Author    :亮亮
a = [1, 2, 3, 4]
b = [6, 7, 8, 9]


def f(x, y):
    return x * y


def main():
    it = map(f, a, b)
    print(list(it))


if __name__ == '__main__':
    main()

"""
[6, 14, 24, 36]
"""
