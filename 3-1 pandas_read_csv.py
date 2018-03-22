# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/3/21 0021 09:54'

import numpy as np
from pandas import DataFrame
# df = pd.read_csv('./data/HR.csv')

# print(df.head())

header = ['subjects', '1ATms', '1AL,mm', ' V_in,mm/ms', '2AT,ms', '2AL,mm', 'V_out,mm/ms', 'HC_time,ms', 'DA,mm',
          'PD ,mm', ' HC_r,mm', ' V_inward,mm/ms', 'V_creep,mm/ms', 'CCD,mm', 'MA,mm^2', 'MA_time,mm/ms',
          ' A_absorbed', 'S_TSC', 'CCT']
checked_video_name = 'corneal_demo'
bio_params_1 = {'The first applanation time, 1AT,ms': '8.09 ', 'The first applanation length, 1AL,mm': '2.95 ', 'The first applanation velocity, V_in,mm/ms': '0.083 ', 'The second applanation time, 2AT,ms': '21.71 ', 'The second applanation length, 2AL,mm': '3.33 ', 'The second applanation velocity, V_out,mm/ms': '0.101 ', 'Start ==> highest concavity time, HC_time,ms': '14.55 ', 'Deformation amplitude, DA,mm': '0.96 ', 'Peak distance, PD ,mm': '4.84'}
bio_params_2 = {'Central highest curvature radius, HC_r,mm': '9.94 ', 'Corneal inward velocity, V_inward,mm/ms': '0.149 ', 'Corneal creep rate, V_creep,mm/ms': '-0.341 ', 'Corneal contour deformation, CCD,mm': '0.13 ', 'Maximum deformation area, MA,mm^2': '3.35 ', 'Maximum deformation area time, MA_time,mm/ms': '11.32 ', 'Energy absorbed area, A_absorbed': '0.62 ', 'Tangent stiffness coefficient,S_TSC': '0.030 ', 'Central corneal thickness, CCT': '#'}

a =[checked_video_name]
b = list(bio_params_1.values())
c = list(bio_params_2.values())
d = np.hstack([a,b,c])
flag = 0

for x in range(2):
    df = DataFrame(d).T
    if flag == 0:
        df.to_csv('a.csv', mode='a', index=None, header=header)
        flag +=1
    else:
        df.to_csv('a.csv', mode='a', index=None, header=False)