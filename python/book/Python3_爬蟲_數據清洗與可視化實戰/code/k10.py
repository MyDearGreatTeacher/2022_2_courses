import pandas as pd

# 还是读取这份文件
df = pd.read_csv("E:/Data/practice/taobao_data.csv", delimiter=',', encoding='utf-8', header=0)

# 计算'成交量'按'位置'分组的平均值
grouped1 = df['成交量'].groupby(df['位置']).mean()
# print(grouped1)

# 计算'成交量'先按'位置'再按'卖家'分组后的平均值
grouped2 = df['成交量'].groupby([df['位置'], df['卖家']]).mean()
print(grouped2)

# 计算先按'位置'再按'卖家'分组后的所有指标(如果可以计算平均值)的平均值
grouped3 = df.groupby([df['位置'], df['卖家']]).mean()
# print(grouped3)
