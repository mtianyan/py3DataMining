# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/4/14 0014 15:12'

import pandas as pd

import numpy as np

df = pd.read_csv('data/HR.csv')

print(df.head(5))

np_s = df['number_project']

print(np_s[np_s.isnull()])
# 空的表示没有空值。

# 均值 3.8
print(np_s.mean())

# 标准差
print(np_s.std())

# 最大值
print(np_s.max())

# 最小值
print(np_s.min())

# 中位数
np_s.median()

# 偏态系数: 122
np_s.skew() # 正偏，大部分小于均值

# 峰度系数: 相对于正态分布，非常尖锐，不靠谱
np_s.kurt()

# 因为是离散的数字。我们可以使用value_counts数每个独立的数字出现了多少次
np_s.value_counts()

# 有时候我们不关心它出现的次数，而是关心它出现的比例
np_s.value_counts(normalize=True)

# 对于数据进行排序
np_s.value_counts(normalize=True).sort_index()
