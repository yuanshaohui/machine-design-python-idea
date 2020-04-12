#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :高阶函数_简单运用事例.py
# @Time      :2020/4/12 19:23
# @Author    :亮亮


def add(x, y, f):
    return f(x)+f(y)


if __name__ == '__main__':
    print(add(1, 2, abs))
