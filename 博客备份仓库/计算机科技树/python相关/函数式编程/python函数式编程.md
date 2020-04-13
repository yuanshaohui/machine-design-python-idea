# python函数式编程

## 一：简介

函数式编程是一种编程范式，一般用于纯逻辑的编程框架，可以简化代码。

## 二：资料来源

[**知乎**](https://zhuanlan.zhihu.com/p/54836224)

[**B站视频**](https://www.bilibili.com/video/BV18E411F7YA?from=search&seid=15826476053320498328)

### 代码：

[gitee代码仓库](https://gitee.com/bright_liang_liang/non_standard_equipment_design/tree/master/%E5%8D%9A%E5%AE%A2%E5%A4%87%E4%BB%BD%E4%BB%93%E5%BA%93/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E6%8A%80%E6%A0%91/python%E7%9B%B8%E5%85%B3/%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B)

[github](https://github.com/yuanshaohui/machine-design-python-idea/tree/master/%E5%8D%9A%E5%AE%A2%E5%A4%87%E4%BB%BD%E4%BB%93%E5%BA%93/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E6%8A%80%E6%A0%91/python%E7%9B%B8%E5%85%B3/%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B)

## 三：内容

### 1. 高阶函数

- 变量名代替函数名
- 函数名和变量名会冲突

```python
def main():
    
    f = abs  # 变量名代替函数名
    print(f(-10))
    

if __name__ == '__main__':
    main()
```

### 2. 简单事例

```python
def add(x, y, f):
    return f(x)+f(y)


if __name__ == '__main__':
    print(add(1, 2, abs))
```

### 3. python内建高阶函数

map.reduce.filter.sorted

#### **map**

**功能**：将一个列表中的每个元素经过一个函数，再重新生成新的函数。（加工）

**传统实现方法**

```python
a = [1, 2, 3, 4]
new_list = []


def f(x):
    return x ** 2


def main(f, a):
    """
    输入一个列表，将每个元素输入一个函数，再输出一个列表
    :return: list
    """
    for i in a:
        new_list.append(f(i))


if __name__ == '__main__':
    main(f, a)
    print(new_list)
```

**函数式编程**

功能：将列表中的数字平方

```python
int_list = [1, 2, 3, 4]


def a(x):
    return x ** 2


def main():
    it = map(a, int_list)  # it是一个可迭代对象
    print(type(it))
    print(list(it))


if __name__ == '__main__':
    main()
"""
<class 'map'>
[1, 4, 9, 16]
"""    
```

功能：将列表中的数字转化为字符串

```python
int_list = [1, 2, 3, 4]


def main():
    it = list(map(str, int_list))
    print(it)


if __name__ == '__main__':
    main()

"""
['1', '2', '3', '4']
"""
```

功能：将两个列表，分别代数加工函数的两个参数，将返回值输出为表。

两个列表相乘

 ```python
a = [1, 2, 3, 4]
b = [6, 7, 8, 9]


def f(x, y):
    return x * y


def main():
    it = map(f, a, b)  # 若列表长度不相同，只取最短的	
    print(list(it))


if __name__ == '__main__':
    main()
    
"""
[6, 14, 24, 36]
"""
 ```

#### reduce函数

功能：（套娃，叠加）将拥有两个传入参数的函数，输入一组数列。数列每个值将于前一个结果再输入该函数。

```python
from functools import reduce

# 求和
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x, y):
    return x + y


def main():
    it = reduce(f, a)
    print(it)


if __name__ == '__main__':
    main()
```

**功能**：将列表中的每个数字，拼成一个数字

```python
from functools import reduce
# 将列表中的每个数字拼成一个整数
a = [1, 2, 3, 4]


def f(x, y):
    return x*10+y


def main():
    it = reduce(f, a)
    print(it)


if __name__ == '__main__':
    main()
    
"""
1234
"""
```

#### filter

功能：（筛选）一个函数，一个列表。函数返回的为判断，若为Ture则保留。

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def fun(x):
    return x % 2 == 1


def main():
    it = filter(fun, a)  # it是一个可迭代对象
    print(list(it))


if __name__ == '__main__':
    main()

"""
[1, 3, 5, 7, 9]
"""
```

#### sorted

功能：进行排序，默认升序

```python
a = [1, 2, 3, 4, 5, 7, 6, 8]


def main():
    it = sorted(a, reverse=True)  # 若逆序则修改参数
    print(it)


if __name__ == '__main__':
    main()
    
"""
[8, 7, 6, 5, 4, 3, 2, 1]
"""
```

功能：按照key自定义函数，来指定列表排序方式

```python
a = [1, -2, 3, 4, -5, 7, 6, 8]


def main():
    it = sorted(a, key=abs, reverse=True)  # 若逆序则修改参数
    print(it)


if __name__ == '__main__':
    main()
    
"""
[8, 7, 6, -5, 4, 3, -2, 1]
"""
```

### 4.匿名函数

**简介**：没有函数名字的函数

**格式**：`lambda 参数1，参数2：【表达式】`

**示例**

```python
f = lambda a, b, c: a + b + c
print(f(1, 2, 3))

"""
6
"""
```

功能：对年龄进行排序

```python
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
```

### 5.闭包

- **定义**：闭包就是一个函数(主要作用就是，不修改源代码的前提下添加新功能)
- 有函数的嵌套（即要有外部函数，也要有内部函数）
- 内部函数中要有外部函数的变量
- 外部函数必须要有返回值，返回外部函数名

**实例**：两个数的和

```python
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
```

**主要功能**：不修改源代码的前提下，增加功能

```python
def add(a, b):
    c = a + b
    print("运算结果是{}".format(c))


def funcOut(func):
    def funcIn(a, b):
        print("这是新增的功能")
        func(a, b)

    return funcIn


add = funcOut(add)


def main():
    add(1, 2)


if __name__ == '__main__':
    main()

"""
这是新增的功能
运算结果是3
"""
```

### 6.装饰器

**功能**：简化闭包的调用(相当于给函数打补丁)

相当于替换了闭包中的`add = funcOut(add)`

**位置**：放在定义的函数之前。`@funcOut`

### 7. 带参数的装饰器

```python
def funcOut(func):
    def funcIn(a, b):
        print("这是新增的功能")
        func(a, b)
```

### 8. 通用装饰器

```python
def funcOut(func):
    def funcIn(*args):
        print("这是新增的功能")
        func(*args)
```

### 9.偏函数

**功能**：快速构建新函数，将旧函数的一些属性固定打包

```python
from functools import partial
new_int = partial(int, base=2)
print(new_int("1010"))
```

