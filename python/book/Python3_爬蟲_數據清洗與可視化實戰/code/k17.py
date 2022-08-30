import pandas as pd

# 读取杭州天气数据
df = pd.read_csv('E:/Data/practice/hz_weather.csv')
# 检测重复行,生成bool的DF
s_isdup = df.duplicated()
# print(s_isdup)
# print(s_isdup.value_counts())  # 全是False

# 检测最高气温重复的行
s_isdup_zgqw = df.duplicated('最高气温')
# print(s_isdup_zgqw.value_counts())

# 去除'最高气温'重复的行
df_dup_zgqw = df.drop_duplicates('最高气温')
# print(df_dup_zgqw)
