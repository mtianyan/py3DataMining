# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/3/22 0022 16:11'

import pandas as pd

import numpy as np

df = pd.read_csv('data/HR.csv')

print(df.head(5))

# 异常值分析: 对于数值型来说，null 就是异常值
sl_s =df['satisfaction_level']

# isnull列出里面有没有null值
print(sl_s.isnull())
print('*******************')

# 列出具体的nan值是哪一行
print(sl_s[sl_s.isnull()])
print('*******************')

# 查看nan值这两行整体
print(df[df['satisfaction_level'].isnull()])
print('*******************')

# 可以将这种nan数据直接drop掉
sl_s = sl_s.dropna()
print(sl_s)
print('*******************')

# 除过丢弃，我们也可以给它填入我们自己的值
# sl_s = sl_s.fillna()

# 查看均值
print(sl_s.mean())

# 标准差
print(sl_s.std())

# 最大值
print(sl_s.max())

# 最小值
print(sl_s.min())

# 可以看到它是一个零到一之间的分布

# 中位数
sl_s.median()

# 下四分位数
sl_s.quantile(q=0.25)

# 上四分位数
sl_s.quantile(q=0.75)

# 偏态系数: 负偏是均值偏小，大部分数比均值要大
sl_s.skew()

# 峰度系数: 相对于正态分布，较为平缓
sl_s.kurt()

# 获取离散化的分布。这串数字。
# 第一个参数是我们要切分的值，
np.histogram(sl_s.values, bins=np.arange(0, 1.1, 0.1))

# 表示从0到0.1的数有195个。这个数就是它的一个分布，分布间隔0.1
# 大致上后面的数是要比前面的数要多的。符合负偏

# 通过异常值处理和直方图绘制的分布分析方法，对satisfaction_level进行了简单分析
# 异常值分析 & 分布分析 知识点。





