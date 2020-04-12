#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :lambda_姓名排序.py
# @Time      :2020/4/12 21:42
# @Author    :亮亮
# @说明       :对每个学生对象的年龄进行排序
# @总结       :


class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def main():
    stu1 = Student("张三", 16)
    stu2 = Student("李四", 22)
    stu3 = Student("王五", 33)
    it = sorted([stu1, stu2, stu3], key=lambda x: x.number)
    maps = map(lambda x: x.name, it)
    print(list(maps))


if __name__ == '__main__':
    main()

"""
['张三', '李四', '王五']
"""
