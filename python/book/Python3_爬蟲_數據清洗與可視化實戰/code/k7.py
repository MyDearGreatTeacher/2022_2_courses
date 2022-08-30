import requests
import urllib.request
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By  # 用于指定HTML文件中的DOM元素
from selenium.webdriver.support.ui import WebDriverWait  # 用于等待网页加载完成
from selenium.webdriver.support import expected_conditions as EC  # 用于指定标志网页加载结束的条件

'''
去哪网PC端自由行 https://fh.dujia.qunar.com/?tf=package
ChromeDriver下载 https://npm.taobao.org/mirrors/chromedriver
'''

# 出发地城市列表
dep_citys = ['北京', '上海', '杭州', '南京', '深圳', '成都']


# 每次发送请求隔一会(模拟用户的输入和检查较慢)
def get_resp(url):
    time.sleep(5)
    return requests.get(url)


if __name__ == '__main__':
    # 控制循环次数
    j = k = 0
    # 用驱动打开Chrome浏览器
    driver = webdriver.Chrome()
    # 对每个出发地
    for dep in dep_citys:
        url = 'https://touch.dujia.qunar.com/golfz/sight/arriveRecommend?dep={}&exclude=&extensionImg=255,175'.format(
            urllib.request.quote(dep))
        response = get_resp(url)
        # 查询到的就是该出发地选定后供选择的若干目的地
        arrv_dict = response.json()
        for data_it in arrv_dict['data']:  # 这里得到的是列表中的一项项dict
            j += 1
            if j > 4:
                break
            for subMod_it in data_it['subModules']:  # 该dict里面subModules列表里的每一项
                k += 1
                if k > 6:
                    break
                for item_it in subMod_it['items']:  # 该项的item字段所示列表的每一项
                    # 通过浏览器打开网页
                    driver.get('https://fh.dujia.qunar.com/?tf=package')
                    # WebDriverWait(driver, 10)意思是使driver保持等待,最多10秒
                    # .until()里指定等待的是什么事件
                    # EC.presence_of_element_located()里面指定标志等待结束的DOM元素
                    # 里面传入元组(By.ID, "depCity")意思是等待id="depCity"的元素加载完成
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "depCity")))
                    # 在Chrome检查元素后,直接右键Copy XPath即可选择相应的元素!
                    # 将出发地清空
                    driver.find_element_by_xpath("//*[@id='depCity']").clear()
                    # 将出发地写进去
                    driver.find_element_by_xpath("//*[@id='depCity']").send_keys(dep)
                    # 将目的地写进去
                    driver.find_element_by_xpath("//*[@id='arrCity']").send_keys(item_it['query'])
                    # 点击[开始定制]按钮
                    driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[3]/div/div[2]/div/a").click()
                    print("dep:%s arrv:%s" % (dep, item_it['query']))
                    # 最多抓3页
                    for i in range(3):
                        time.sleep(random.uniform(5, 6))  # 随机等待5~6秒,模拟用户每页看个五六秒
                        # 关于[下一页]按钮:在不同的页上,下一页按钮的XPath是不一样的,比如下面两个
                        # // *[ @ id = "pager"] / div / a[8]
                        # // *[ @ id = "pager"] / div / a[7]
                        # 因此不能通过这种方式来实现点击下一页
                        # 可以用XPath获得翻页的整块元素,然后在其中找'下一页'按钮
                        page_btn_a_s = driver.find_elements_by_xpath('//*[@id="pager"]/div/a')
                        # 如果获取不到页码按钮,说明从出发地到目的地没有产品,直接跳出
                        if not page_btn_a_s:
                            break
                        # 旅行方案产品列表
                        routes = driver.find_elements_by_xpath('//*[@id="list"]/div')
                        # 如果第一页就没有旅行产品(如北京到泰国),那么后面的页也不会有
                        if not routes:
                            break
                        for route in routes:
                            result = {
                                'date': time.strftime('%Y-%m-%d', time.localtime(time.time())),
                                'dep': dep,
                                'arrv': item_it['query'],
                                'result': route.text
                            }
                            print(result)  # 这里可以做存到数据库的操作
                        has = False  # 记录是否找得到'下一页'
                        for a in page_btn_a_s:
                            if a.text == u"下一页":
                                has = True
                                a.click()
                                break
                        if not has:  # 如果没找到下一页
                            break  # 说明已经是最后一页,结束这一系产品的循环
