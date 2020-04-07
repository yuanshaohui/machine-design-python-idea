# python自动化办公

## 一： 学习原因

1. 本身具有一定的python基础
2. 爬虫数据存储与展示的需要，当然后期会学习数据库存储。
3. 平时办公软件用的比较多
4. 想制作一个自动化生成产品说明文档的软件

## 二：学习阶段与最终目标

- [ ] 对world操控
- [ ] 对excel操控
- [ ] 对ppt操控
- [ ] 设计出解决日常使用的问题
- [ ] 设计出减速箱课程设计生成软件

## 三：python环境及知识前置

- 版本：[python3.7](https://www.python.org/)
- 前置知识：[python基础](https://www.bilibili.com/video/BV1zE41137Nm?from=search&seid=1561936263328028962)
- 基本库
  - xlrd（excel读取操作库）
  - xlwt（excel写入操作库）
  - xlutils(xl工具集，将excel模板格式放在新建文件中的)

> **注意**：1. xlutils对新格式"xlsx"支持不行

## 四：python操作excel表格

### excel文件的结构

- 工作簿
  - 工作表
    - 单元格

### 查询单元格内容

代码功能：可以查看该excle中的单元格内容

```python
import xlrd

def main():

    xlsx = xlrd.open_workbook("F:/360MoveData/Users/浪浪/Desktop/name.xls")
    table = xlsx.sheet_by_index(0)
    # table = xlsx.sheet_by_index("这是第一个表")
    print(table.cell_value(0, 0))

if __name__ == "__main__":
    main()
```

> 小技巧：想看到每一列的数字，在excle中---设置----公式----使用公式R1C1

### 往单元格写入内容

代码功能：新建表格并写入

```python
import xlwt

def main():

    new_workbook = xlwt.Workbook()  # 创建新的工作表对象
    worksheet = new_workbook.add_sheet('new_sheet')  # 创建"new_sheet"工作表
    worksheet.write(0, 0, "test")  # 往单元格内写入内容
    new_workbook.save("F:/360MoveData/Users/浪浪/Desktop/test.xls")

if __name__ == "__main__":
    main()
```

### 控制表格中的格式



## 五：感谢及资源地址

**感谢**：B站野生技术协会

**原文链接**：[用Python自动办公，做职场高手](https://www.bilibili.com/video/BV1QJ411h7PQ?p=13)