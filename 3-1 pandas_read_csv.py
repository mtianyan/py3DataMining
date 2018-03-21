# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/3/21 0021 09:54'

import pandas as pd
from pandas import DataFrame
df = pd.read_csv('./data/HR.csv')

print(df.head())

a = [20, 'male', 'mtianyan', '汉字']
df = DataFrame(a)
df = df.T
df.to_csv('a.csv', mode='a', index=None, header=False)