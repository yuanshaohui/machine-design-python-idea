#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :map的应用3.py
# @Time      :2020/4/12 20:16
# @Author    :亮亮
int_list = [1, 2, 3, 4]


def main():
    it = list(map(str, int_list))
    print(it)


if __name__ == '__main__':
    main()

"""
['1', '2', '3', '4']
"""
