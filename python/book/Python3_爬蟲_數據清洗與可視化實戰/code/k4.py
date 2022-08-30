import base64
import csv
import hashlib
import time
import pymongo
import requests

'''
和风天气3-10天天气预报API https://www.heweather.com/douments/api/s6/weather-forecast
和风天气加密签名认证 https://www.heweather.com/documents/api/s6/sercet-authorization
JSON在线结构化工具 http://www.json.org.cn/tools/JSONEditorOnline/index.htm
和风天气控制台(看剩余访问量和key和用户ID) https://console.heweather.com/my/service
城市代码ID下载 http://www.heweather.com/documents/city
'''

mykey = '80ba7933049a4065b687893a7619e909'
city_id = []  # 记录城市id的列表


# API的一般使用方式
def weather_api(location, key):
    url = 'https://free-api.heweather.com/s6/weather/forecast?location=' + location + '&key=' + key
    response = requests.get(url)
    response.encoding = 'utf8'  # 设定Respons对象的编码方式
    # print(response.text)
    return response


# 和风天气签名生成算法-Python版本
# params API调用的请求参数集合的字典(全部需要传递的参数组成的字典),不包含sign参数
# secret 用户的认证 key
# return string 返回参数签名值
def gen_sign(params, secret):
    canstring = ''
    # 先将参数以其参数名的字典序升序进行排序
    # 字典的items()函数以列表返回可遍历的(键,值)元组数组
    params = sorted(params.items(), key=lambda item: item[0])
    # 遍历排序后的参数数组中的每一个key/value对
    for k, v in params:
        # 不能包含sign或者key或者空字符串key.sign是要计算生成的,而key只用来计算sign,防止暴露给第三方
        if k != 'sign' and k != 'key' and v != '':
            canstring += k + '=' + v + '&'  # URL里面的GET参数就是这样的
    canstring = canstring[:-1]  # 用切片去除最后多余的一个'&'符
    canstring += secret  # 尾接key
    # 在MD5对象创建前需要对数据进行编码
    canstring = canstring.encode('utf8')
    # 用这个拼接后的字符串创建一个md5对象,然后digest()方法返回md5的byte格式
    md5 = hashlib.md5(canstring).digest()
    # 对其进行base64编码并返回,现在返回的就是加密签名sign的value了
    return base64.b64encode(md5)  # 这个方法需要的是一个byte对象


# API的加密签名使用方式
def weather_api_sign(location, key, username='HE1811071811441319'):
    # 获取10位时间戳,即取当前time()结果的整数部分
    timestamp = int(time.time())
    # 请求参数,不包含key也不包含sign
    params = {'location': location, 'username': username, 't': str(timestamp)}
    # 计算签名,并添加到请求参数字典中.注意byte转换成字符串才能用于后面的字符串拼接
    sign = gen_sign(params, key)
    sign = str(sign, 'utf8')
    # 我发现有时会出现{"HeWeather6":[{"status":"sign error"}]}即签名不正确
    # 这是因为sign里可能出现'+'号导致的,在传输时'+'会被视为' ',因此需要做url转义成'%2b'
    sign = str.replace(sign, '+', '%2B')
    params['sign'] = sign  # 现在得到的就是正确的签名了,将其放入参数字典中
    # 从字典构造URL,然后对其发送GET请求
    url = 'https://free-api.heweather.com/s6/weather/forecast?'
    for k, v in params.items():
        url += k + '=' + v + '&'
    url = url[:-1]  # 去除最后多余的一个'&'符
    # print(url)
    response = requests.get(url)
    response.encoding = 'utf8'  # 设定Respons对象的编码方式
    # print(response.text)
    return response


# 从下载的csv文件中读取城市id列表
def city_id_csv():
    global city_id
    # 解决'gbk' codec can't decode byte 0xad in position 256: illegal multibyte sequence
    csv_file = csv.reader(open('china-city-list.csv', 'r', encoding='UTF-8'))
    # print(type(csv_file))  # <class '_csv.reader'>
    # 用枚举使在for-in循环中能考察其循环次数
    for i, line in enumerate(csv_file):
        if i > 1:  # 这是为了跳过前两行表头
            city_id.append(line[0])
        if i > 30:  # 不妨只取少量城市,只是实现功能(现在免费用户一天最多才1000次天气查询)
            break


# 连接到本地MongoDB中的数据库(如果不存在即创建),并向其中写入数据.要先调用填充city_id列表的函数
def sto_in_local_mongo():
    # 连接到本地MongoDB
    client = pymongo.MongoClient('localhost', 27017)
    # 天气数据库
    db_weather = client['weather']
    # 天气数据库中的数据表
    sheet_weather = db_weather['sheet_weather_3']
    # 写入
    for id in city_id:
        city_weather = weather_api_sign(id, mykey)
        dic = city_weather.json()  # Response对象的json格式以字典存储
        print(dic)
        sheet_weather.insert_one(dic)  # 写入数据库
        time.sleep(1)


if __name__ == '__main__':
    # weather_api('CN101010100', mykey)
    # weather_api_sign('CN101010100', mykey)
    # city_id_csv()  # 从本地csv文件读取城市编号
    # sto_in_local_mongo()  # 查询城市天气并存储到本地
    # 从本地使用数据库中的数据
    Client = pymongo.MongoClient('localhost', 27017)
    Db_Weather = Client['weather']
    Sheet_Weather = Db_Weather['sheet_weather_3']
    # 如查询北京的数据如下.这里的'.0'可以省略
    for item in Sheet_Weather.find({'HeWeather6.0.basic.parent_city': '北京'}):
        print(item)
