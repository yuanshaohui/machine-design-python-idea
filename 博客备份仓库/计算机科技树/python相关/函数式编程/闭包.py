#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :闭包.py
# @Time      :2020/4/12 22:09
# @Author    :亮亮
# @说明       :利用闭包来实现两个数的和
# @总结       :


def add(a, b):
    return a + b


def fun_out(num1):
    def fun_in(num2):
        return num1 + num2

    return fun_in


def main():
    f = fun_out(100)
    print(f(200))


if __name__ == '__main__':
    main()
