# anacoda的简单使用

## 一：简介

anacoda是一个python包管理工具，具有丰富的python库的安装。

- 创建不同的环境，管理版本和库（**主要**）
- 数据分析

## 二：主要操作指令

|           功能           |                   操作                   |
| :----------------------: | :--------------------------------------: |
| 查看环境变量是否安装成功 |            `conda --version`             |
|  将所有的工具包进行升级  |          `conda upgrade --all`           |
|       创建虚拟环境       | `conda create -n [name] python=[版本号]` |
|  查看所有创建的虚拟环境  |             `conda info -e`              |
|        查看环境二        |             `conda env list`             |
|         删除环境         |      `conda remove -n [name] --all`      |
|         进入环境         |            `activate [name]`             |
|    查看环境中的所有包    |               `conda list`               |
|         导出环境         |  `conda env export > environment.yaml`   |
|         导入环境         |  `conda env create -f environment.yaml`  |



