import requests

'''
中国旅游网 /www.cntour.cn
'''

url = 'http://www.cntour.cn'
response = requests.get(url)  # 用GET方式获取访问该网站的响应
# print(type(response))  # <class 'requests.models.Response'>
# print(type(response.text))  # <class 'str'>
print(response.text)  # 其中包含了HTML字符串
