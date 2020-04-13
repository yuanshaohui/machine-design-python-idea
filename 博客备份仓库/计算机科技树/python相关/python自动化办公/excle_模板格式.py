#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :excle_模板格式.py
# @Time      :2020/4/13 20:21
# @Author    :亮亮
# @说明       :创建模板，保存并使用
# @总结       :
from xlutils.copy import copy
import xlrd
import xlwt


def main():
    old_excel = xlrd.open_workbook("F:/360MoveData/Users/浪浪/Desktop/测试/test.xls", formatting_info=True)

    new_excel = copy(old_excel)  # 将原来工作簿的内容复制到新的工作簿
    new_sheet = new_excel.get_sheet(0)  # 将工作表复制过来

    style = xlwt.XFStyle()  # 创建新的空格式模板对象(存放字体对象，框线对，他的每个属性也为对象)

    # 字体
    font = xlwt.Font()  # 创建字体对象
    font.name = "微软雅黑"  # 写入对象的属性
    font.bold = True
    font.height = 360
    style.font = font

    # 边框
    borders = xlwt.Borders()
    borders.top = xlwt.Borders.THIN  # THIN代表的不同样式，如粗细
    borders.bottom = xlwt.Borders.THIN  # THIN代表的不同样式，如粗细
    borders.left = xlwt.Borders.THIN  # THIN代表的不同样式，如粗细
    borders.right = xlwt.Borders.THIN  # THIN代表的不同样式，如粗细
    style.borders = borders

    # 对齐
    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.HORZ_CENTER
    style.alignment = alignment

    new_sheet.write(2, 2, 1, style)
    new_sheet.write(3, 2, 2, style)
    new_sheet.write(4, 2, 3, style)
    new_sheet.write(5, 2, 4, style)
    new_excel.save("F:/360MoveData/Users/浪浪/Desktop/测试/test3.xls")


if __name__ == '__main__':
    main()
