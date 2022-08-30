import time

# 从格林威治时间到现在,单位秒
print('系统时间戳:', time.time())

print('本地时间按格式转成str:', time.strftime('%Y-%m-%d %X', time.localtime()))

# 无参的localtime返回time.struct_time格式的时间,是本地时区的时间
print('无参localtime:', time.localtime())

print('本时区时间转成时间戳:', time.mktime(time.localtime()))

# 将时间戳转换为能读懂的时间
print('时间戳转时间:', time.strftime('%Y-%m-%d %X', time.localtime(time.time())))
