# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/4/14 0014 15:37'

import pandas as pd

import numpy as np

df = pd.read_csv('data/HR.csv')

print(df.head(5))

tsc_s = df['time_spend_company']

tsc_s.value_counts().sort_index()
# 呆了三年的人最多

# 查看平均数
tsc_s.mean()

