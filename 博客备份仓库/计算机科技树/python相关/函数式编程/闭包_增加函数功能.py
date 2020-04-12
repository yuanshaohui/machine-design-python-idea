#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :闭包_增加函数功能.py
# @Time      :2020/4/12 22:35
# @Author    :亮亮
# @说明       :在不改变源码的基础上，进行功能增加
# @总结       :


def add(a, b):
    c = a + b
    print("运算结果是{}".format(c))


def funcOut(func):
    def funcIn(a, b):
        print("这是新增的功能")
        func(a, b)

    return funcIn


add = funcOut(add)


def main():
    add(1, 2)


if __name__ == '__main__':
    main()

"""
这是新增的功能
运算结果是3
"""