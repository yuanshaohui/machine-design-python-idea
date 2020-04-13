#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :excle_查看单元格中的内容.py
# @Time      :2020/4/13 20:02
# @Author    :亮亮
# @说明       :查看单元格中的内容
# @总结       :将工作簿和工作表当成对象进行操作
import xlrd


def main():
    xlsx = xlrd.open_workbook("F:/360MoveData/Users/浪浪/Desktop/测试/test.xls")
    table = xlsx.sheet_by_index(0)
    value = table.cell_value(0, 0)
    print(value)


if __name__ == '__main__':
    main()