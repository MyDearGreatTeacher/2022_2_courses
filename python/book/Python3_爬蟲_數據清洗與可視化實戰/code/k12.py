import pandas as pd
import numpy as np

# 读取杭州天气文件
df = pd.read_csv("E:/Data/practice/hz_weather.csv", delimiter=',', encoding='utf-8', header=0)

# (1)DataFrame转Series(层次化索引)
s = df.stack()
# print(type(s))  # <class 'pandas.core.series.Series'>

# (2)Series转回DataFrame
df = s.unstack()

# (3)数据透视表:以日期为索引
df1 = df.set_index('日期')
print(df1.head())

# (4)数据透视表:以[天气]为索引,查看不同[风向]下的[最高气温]的[最大值]
df2 = pd.pivot_table(df, index=['天气'], columns=['风向'], values=['最高气温'], aggfunc=np.max)
print(df2)
