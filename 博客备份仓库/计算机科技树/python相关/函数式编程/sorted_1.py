#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :sorted_1.py
# @Time      :2020/4/12 21:14
# @Author    :亮亮
# @说明       :sorted函数进行排序
# @总结       :
a = [1, 2, 3, 4, 5, 7, 6, 8]


def main():
    it = sorted(a, reverse=True)  # 若逆序则修改参数
    print(it)


if __name__ == '__main__':
    main()

"""
[8, 7, 6, 5, 4, 3, 2, 1]
"""
