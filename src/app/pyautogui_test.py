# -*- coding: utf-8 -*-
# @Time     : 2020/7/22 22:26
# @Author   : XieYao
# @Software : PyCharm
import time

import pyautogui as auto
from datetime import datetime

from util.autogui_enum import OffsetDirectionEnum, MouseOperationEnum
from util.autogui_util import autoGuiUtil
import pyperclip


def mapping_image(image, operation):
    box_location = auto.locateOnScreen(image)
    image_center = auto.center(box_location)
    if operation == "double_click":
        auto.doubleClick(image_center)
    else:
        auto.leftClick(image_center)


def baidu_search():
    right_50_down_10 = {OffsetDirectionEnum.right: 50, OffsetDirectionEnum.down: 10}
    this_ret = autoGuiUtil.mapping_by_cv2('../../file/pic/google_search.PNG', MouseOperationEnum.single_click, right_50_down_10 , 10)
    if this_ret:
        autoGuiUtil.text_input("www.baidu.com")
        auto.press("enter")
    right_50_down_100 = {OffsetDirectionEnum.right: 50, OffsetDirectionEnum.down: 100}
    this_ret = autoGuiUtil.mapping_by_cv2('../../file/pic/baidu_search.PNG', MouseOperationEnum.single_click,
                                          right_50_down_100, 10)
    if this_ret:
        autoGuiUtil.text_input("你好呀")
        auto.press("enter")



def cal_test_ori():
    mapping_image('../../file/pic/cal_7.PNG', MouseOperationEnum.single_click)
    mapping_image('../../file/pic/cal_multi.PNG', 'single_click')
    mapping_image('../../file/pic/cal_9.PNG', 'single_click')
    mapping_image('../../file/pic/cal_equal.PNG', 'single_click')


def cal_test_cv2():
    autoGuiUtil.mapping_by_cv2('../../file/pic/cal_7.PNG', 'single_click')
    autoGuiUtil.mapping_by_cv2('../../file/pic/cal_multi.PNG', 'single_click')
    autoGuiUtil.mapping_by_cv2('../../file/pic/cal_9.PNG', 'single_click')
    autoGuiUtil.mapping_by_cv2('../../file/pic/cal_equal.PNG', 'single_click')

def add_new_page_test():
    offset_dict = {OffsetDirectionEnum.right: 10, OffsetDirectionEnum.down: 10}
    autoGuiUtil.mapping_by_cv2("../../file/pic/add_new_page.PNG", MouseOperationEnum.single_click, offset_dict)


if __name__ == '__main__':
    start_time = datetime.now()
    add_new_page_test()
    baidu_search()
    # add_new_page_test()
    end_time = datetime.now()
    print("耗时：" + str((end_time - start_time).seconds) + 's ' + str((end_time - start_time).microseconds))
