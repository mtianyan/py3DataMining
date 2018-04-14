# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/4/14 0014 14:56'

import pandas as pd

import numpy as np

df = pd.read_csv('data/HR.csv')

print(df.head(5))

le_s = df['last_evaluation']

# 查看它有没有空值
print(le_s[le_s.isnull()])
# Series([], Name: last_evaluation, dtype: float64) 返回空，说明没有空值。

# 均值 67
print(le_s.mean())

# 标准差
print(le_s.std())

# 最大值
print(le_s.max())

# 最小值
print(le_s.min())

# 中位数
le_s.median()

# 偏态系数: 122
le_s.skew() # 均值要比大部分值多很多

# 峰度系数: 相对于正态分布，非常尖锐，不靠谱
le_s.kurt()

# 我们的第一印象是在0-1之间，但是平均数等都出现了异常。我们需要看看大于1的数有
print(le_s[le_s > 1])
# 99999 去掉这个值

# 去除这个大于1的值
le_s = le_s[le_s <= 1]

# 下四分位数
q_low = le_s.quantile(q=0.25)

# 上四分位数
q_high = le_s.quantile(q=0.75)

# 四分位间距 = 上四分位数- 下四分位数
q_interval = q_high - q_low

# 异常值系数k
k = 1.5

# 筛选
le_s = le_s[le_s < q_high+k*q_interval][le_s > q_low-k*q_interval]

print(le_s)

# 只有一条数据是异常值被我们剔除掉了。

# 获取离散化的分布。这串数字。
# 第一个参数是我们要切分的值，第二个参数是我们要切分的临界值
np.histogram(le_s.values, bins=np.arange(0, 1.1, 0.1))

# 去除异常值之后重新算一遍各种数据值

le_s.mean()