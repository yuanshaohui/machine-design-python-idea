#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :map的应用二.py
# @Time      :2020/4/12 20:04
# @Author    :亮亮
int_list = [1, 2, 3, 4]


def a(x):
    return x ** 2


def main():
    it = map(a, int_list)  # it是一个可迭代对象
    print(type(it))
    print(list(it))


if __name__ == '__main__':
    main()
