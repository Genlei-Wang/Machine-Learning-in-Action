#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 13:45
# @Author  : GXl
# @File    : 3.2.1-1.py
# @Software: win10 Tensorflow1.13.1 python3.5.6


from math import log

"""
Parameters:
    无
Returns:
    dataSet - 数据集
    labels - 分类属性
"""
# 函数说明:创建测试数据集
def createDataSet():
    dataSet = [[0, 0, 0, 0, 'no'],#数据集
            [0, 0, 0, 1, 'no'],
            [0, 1, 0, 1, 'yes'],
            [0, 1, 1, 0, 'yes'],
            [0, 0, 0, 0, 'no'],
            [1, 0, 0, 0, 'no'],
            [1, 0, 0, 1, 'no'],
            [1, 1, 1, 1, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [1, 0, 1, 2, 'yes'],
            [2, 0, 1, 2, 'yes'],
            [2, 0, 1, 1, 'yes'],
            [2, 1, 0, 1, 'yes'],
            [2, 1, 0, 2, 'yes'],
            [2, 0, 0, 0, 'no']]
    labels = ['年龄', '有工作', '有自己的房子', '信贷情况']#分类属性
    return dataSet, labels#返回数据集和分类属性

"""
Parameters:
    dataSet - 数据集
Returns:
    shannonEnt - 经验熵(香农熵)
"""
# 函数说明:计算给定数据集的经验熵(香农熵)
def calcShannonEnt(dataSet):
    numEntires = len(dataSet)                       #返回数据集的行数
    labelCounts = {}                                #保存每个标签(Label)出现次数的字典
    for featVec in dataSet:                         #对每组特征向量进行统计
        currentLabel = featVec[-1]                  #提取标签(Label)信息
        if currentLabel not in labelCounts.keys():  #如果标签(Label)没有放入统计次数的字典,添加进去
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1              #Label计数
    shannonEnt = 0.0                                #经验熵(香农熵)
    for key in labelCounts:                         #计算香农熵
        prob = float(labelCounts[key]) / numEntires #选择该标签(Label)的概率
        shannonEnt -= prob * log(prob, 2)           #利用公式计算
    return shannonEnt                               #返回经验熵(香农熵)


if __name__ == '__main__':
    dataSet, features = createDataSet()
    print(dataSet)
    print(calcShannonEnt(dataSet))