# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/4/14 0014 15:19'


import pandas as pd

import numpy as np

df = pd.read_csv('data/HR.csv')

print(df.head(5))

amh_s = df['average_monthly_hours']

print(amh_s[amh_s.isnull()])
# 空的表示没有空值。

# 均值 3.8
print(amh_s.mean())

# 标准差
print(amh_s.std())

# 最大值
print(amh_s.max())

# 最小值
print(amh_s.min())

# 中位数
amh_s.median()

# 偏态系数: 122
amh_s.skew() # 稍微正偏，大部分小于均值

# 峰度系数: 平衡
amh_s.kurt()

# 下四分位数
q_low = amh_s.quantile(q=0.25)

# 上四分位数
q_high = amh_s.quantile(q=0.75)

# 四分位间距 = 上四分位数- 下四分位数
q_interval = q_high - q_low

# 异常值系数k
k = 1.5

# 异常值区间
amh_s = amh_s[amh_s < q_high+ k*q_interval][amh_s > q_low-k*q_interval]

print(amh_s) # 这个属性里是没有异常值的

# 获取离散化的分布。这串数字。
# 第一个参数是我们要切分的值，第二个参数除过前面用过的给一个临界值列表，也可以直接指定分成几份
np.histogram(amh_s.values, bins=10)

# 原来的用法
np.histogram(amh_s.values, bins=np.arange(amh_s.min(), amh_s.max()+10, 10))
# 注意这里需要加上10，否则无法取到最大值。

# 使用value_counts数连续值的数量
amh_s.value_counts( bins=np.arange(amh_s.min(), amh_s.max()+10, 10))

# 通过value_counts获得的是左开右闭的区间。
# 通过hist取得的是左闭右开的。虽然是左闭右开，最后一个数归到之前集合中




