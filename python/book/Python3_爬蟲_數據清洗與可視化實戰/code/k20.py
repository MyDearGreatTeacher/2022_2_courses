import datetime
import numpy as np
import pandas as pd

# pd.date_range()函数用于创建一个Pandas时间序列DatetimeIndex
# start参数(也是第一个参数)传入一个str格式的开始时间,也可以传入一个datetime对象
# 这里用datetime.datetime()创建了一个datetime对象,只用了前三个参数也就是年月日
# pd.date_range()函数可以指明end表示时间序列的结尾时间
# 这里用periods参数指明序列中要生成的时间的个数,freq='D'指定为每天(Day)生成一个时间
dti = pd.date_range(start=datetime.datetime(2018, 11, 14), periods=18, freq='D')
print(dti, '\n', '*' * 40, sep='')

# 将时间序列放在Series对象中作为索引,这里freq='W'表示隔一周生成一个
s_dti = pd.Series(np.arange(6), index=pd.date_range('2018/11/4', periods=6, freq='W'))
print(s_dti.head(), '\n', '*' * 40, sep='')

# 取时序数据中指定时间的内容
print(s_dti['2018-11-25'], '\n', '*' * 40, sep='')

# 取第二个索引对应的时间的年月日
print(s_dti.index[2].year, s_dti.index[2].month, s_dti.index[2].day, '\n', '*' * 40, sep='')
