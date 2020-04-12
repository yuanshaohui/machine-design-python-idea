#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :map的应用.py
# @Time      :2020/4/12 19:31
# @Author    :亮亮
a = [1, 2, 3, 4]
new_list = []


def f(x):
    return x ** 2


def main(f, a):
    """
    输入一个列表，将每个元素输入一个函数，再输出一个列表
    :return: list
    """
    for i in a:
        new_list.append(f(i))


if __name__ == '__main__':
    main(f, a)
    print(new_list)
