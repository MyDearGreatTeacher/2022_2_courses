import pandas as pd
import numpy as np

# 读取去哪网自由行产品数据
df = pd.read_csv("E:/Data/practice/qunar_free_trip.csv", delimiter=',', encoding='utf-8', header=0)
# print(df.head())

# 按'出发地'和'目的地'分组,查看'价格'的均值
# 默认情况下,groupby使用as_index=True,这时将用于分组的列作为(行)索引,生成Series对象
s1 = df['价格'].groupby([df['出发地'], df['目的地']]).mean()
# print(s1)

# 读取路线页数
df_ = pd.read_csv("E:/Data/practice/qunar_route_cnt.csv", delimiter=',', encoding='utf-8', header=0)
# print(df_.head())

# 按'出发地'和'目的地'分组,查看所有指标(如果可求均值)的均值
# 这里指明as_index=False,则不把用于分组的列作为(行)索引
# 相当于仅仅进行了排序,让这些分组相近的排在一起,最终得到的仍然是DataFrame对象
df1 = df.groupby([df['出发地'], df['目的地']], as_index=False).mean()
# print(type(df1))  # <class 'pandas.core.frame.DataFrame'>
# print(df1.head())

# 将均值表和路线表合并,不指定on参数也不指定how参数,则默认寻找相同的列做INNER JOIN
df_ij = pd.merge(df1, df_)
# print(df_ij.head(7))  # 前7行

# 数据透视表:以[出发地]为索引,查看不同[目的地]下的[价格]的[平均值]
df2 = pd.pivot_table(df, index=['出发地'], columns=['目的地'], values=['价格'], aggfunc=np.average)
# print(df2.head(8))

# 数据透视表:在[出发地为杭州的数据中],以[出发地,目的地]为索引(实际上出发地也就只有杭州了)
# 查看不同[去程方式]下[价格]的[平均值]
df3 = pd.pivot_table(df[df['出发地'] == '杭州'], index=['出发地', '目的地'], columns=['去程方式'], values=['价格'], aggfunc=np.mean)
# print(df3)
