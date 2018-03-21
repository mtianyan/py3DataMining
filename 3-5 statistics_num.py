# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/3/21 0021 15:57'

import pandas as pd

df = pd.read_csv('./data/HR.csv')
# 其他可选参数: sep="\t" 不止可以读csv，可以指定其他分隔符

print(type(df))

# 组成df里的每一列数据又是一个Series
print(type(df['satisfaction_level']))
print('*****************************')

# 平均数
print(df.mean())
# 返回的是一个series类型的
print(type(df.mean()))
# 使用series直接求均值,得到一个值
print(df['satisfaction_level'].mean())
print('*****************************')

# 中位数
print(df.median())
# series的中位数
print (df['satisfaction_level'].median())
print('*****************************')

# 分位数
# 四分位数填入0.25
print(df.quantile(q=0.25))
print(df['satisfaction_level'].quantile(q=0.25))
print('*****************************')

# 众数:返回可能有点不同，因为众数有可能不是唯一的.出现几个就会返回几个。
# 对于返回的这个dataframe，它的行数取决于众数最多的那一列
print(df.mode())
print('*****************************')
# 对于series求众数，返回的也是一个series
print(df['satisfaction_level'].mode())
print('*****************************')

# 离中趋势
# 标准差std
print(df.std())
print('*****************************')
print(df['satisfaction_level'].std())
print('*****************************')

# 方差
print(df.var())
print('*****************************')
print(df['satisfaction_level'].var())
print('*****************************')

# 求和：离散数据求和变成了字符串相连
print(df.sum())
print('*****************************')
print(df['satisfaction_level'].sum())
print('*****************************')

# 偏态系数
print(df.skew())
print('*****************************')
# 满意度级别的偏态系数为负的，说明它的平均值偏小，也就是它的大部分值是大于平均值，它是负偏。所以它的satisfaction_level是处于大多数人比较好的状态
print(df['satisfaction_level'].skew())
print('*****************************')

# 峰态系数(针尖还是山丘）
# 这里的峰态系数以正态分布为0作为标准的。也就是减过3了。
print(df.kurt())
print('*****************************')
print(df['satisfaction_level'].kurt())
# -0.67 ,与正态0相比差值不到2，相对平缓的
print('*****************************')


# 分布函数
import scipy.stats as ss

# 生成一个正态分布的对象
ss.norm

# 查看这个正态分布对象的性质
# 'm' = mean, 均值
# 'v' = variance, 方差
# 's' = (Fisher's) skew, 偏态系数
# 'k' = (Fisher's) kurtosis. 峰态系数
print(ss.norm.stats(moments="mvsk"))
# (array(0.0), array(1.0), array(0.0), array(0.0))
# 正态分布均值0，方差1，偏态系数和峰态系数都是0
print('*****************************')


# 指定横坐标，返回纵坐标的值
print(ss.norm.pdf(0.0))
# 0.398942280401这就是这个分布函数在0这一点的值
# 标准正态分布，它的标准差方差是1，均值是0.此时输入0就会得到0.398
print('*****************************')


# 输入值必须在0到1之间，表示一个累积值
print(ss.norm.ppf(0.9))
# 1.28155156554
# 表示从负无穷一直累积到1.28得到的值是0.9
# 从负无穷大到正无穷大积分是1:积分是0.9的时候，积分区间是从负无穷到1.28
print('*****************************')


# 从负无穷积到给定数字的积分大小,累积概率大小
print(ss.norm.cdf(2))
# 0.977249868052
print('*****************************')


# cdf(2)到cdf(-2)之间的积分概率为0.9544
# 两倍的标准差 - 负两倍的标准差。这中间的累积概率
print(ss.norm.cdf(2)-ss.norm.cdf(-2))
print('*****************************')

# 产生正态分布的数字
print(ss.norm.rvs(size=10))

# 卡方分布
ss.chi2

# T分布
ss.t

# f分布
ss.f

# pdf(指定横坐标，返回纵坐标的值)
# ppf(输入值必须在0到1之间，表示一个累积值) :也就是从负无穷到所求未知数字的为输入参数:区间累积概率。
# cdf 给定一个数字，求从负无穷到这个数字区间的累积概率。
# rvs 给出符合某一分布的数字
print('*****************************')


# 抽样
# 按个数
print(df.sample(n=5))
# 按百分比，150 * 0.001 * 100 取15个
print(df.sample(frac=0.001))
print('*****************************')
print(df['satisfaction_level'].sample(5))

# 学习方法，打开官网随用随查
# https://www.scipy.org/
# https://pandas.pydata.org/
# 十分钟接触pandas
# 进阶: http://pandas.pydata.org/pandas-docs/stable/api.html
