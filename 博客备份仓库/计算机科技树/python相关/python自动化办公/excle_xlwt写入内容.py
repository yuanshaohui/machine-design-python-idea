#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :excle_xlwt写入内容.py
# @Time      :2020/4/13 20:11
# @Author    :亮亮
# @说明       :创建新的工作簿并写入内容
# @总结       :
import xlwt


def main():
    new_workbook = xlwt.Workbook()
    new_sheet = new_workbook.add_sheet("new_sheet")
    new_sheet.write(0, 0, "something")
    new_workbook.save("F:/360MoveData/Users/浪浪/Desktop/测试/test2.xls")


if __name__ == '__main__':
    main()
