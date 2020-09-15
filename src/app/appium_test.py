# -*- coding: utf-8 -*-
# @Time     : 2020/7/19 16:14
# @Author   : XieYao
# @Software : PyCharm
from appium import webdriver  #导入webdriver库
import time #导入时间模块

if __name__ == '__main__':
    desired_caps = {} #配置参数的字典
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = 'vivo x20'
    desired_caps['appPackage'] = 'com.youdao.calculator'
    desired_caps['appActivity'] = '.activities.MainActivity'
    # desired_caps['udid'] = 'xxxx' #xxxx不是真的udid，写真的udid
    desired_caps['newCommandTimeout'] = 6000
    desired_caps['noReset'] = 'True'


    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) #第一个参数是默认的，不需要更改（wd 可以理解是WebDriver 的缩写）

    driver.find_element_by_image('../file/pic/cal_7.PNG').click()
    driver.find_element_by_image('../file/pic/cal_multi.PNG').click()
    driver.find_element_by_image('../file/pic/cal_9.PNG').click()
    driver.find_element_by_image('../file/pic/cal_equal.PNG').click()
    # input()

    # time.sleep(30)
    # driver.find_element_by_id("com.android.calculator2:id/digit_1").click()   #通过id找到数字1并且点击
    # driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
    # driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
    # driver.find_element_by_id("com.android.calculator2:id/del").click() #点击删除键
    # driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
    # driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
    # driver.find_element_by_id("com.android.calculator2:id/op_add").click() #点击‘+’
    # driver.find_element_by_id("com.android.calculator2:id/digit_6").click()
    # driver.find_element_by_id("com.android.calculator2:id/eq").click() #点击‘=’

    time.sleep(5) #这个是为了能够看清结果，可删除
    driver.quit()