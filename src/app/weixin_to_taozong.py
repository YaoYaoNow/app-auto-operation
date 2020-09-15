# -*- coding: utf-8 -*-
# @Time     : 2020/7/25 22:05
# @Author   : XieYao
# @Software : PyCharm
from datetime import datetime

from util.autogui_enum import OffsetDirectionEnum, MouseOperationEnum
from util.autogui_util import autoGuiUtil
import time
import pyautogui

if __name__ == '__main__':
    # click search_button
    start_time = datetime.now()
    right_down_10 = {OffsetDirectionEnum.right: 10, OffsetDirectionEnum.down: 10}
    autoGuiUtil.mapping_by_cv2('../../file/weixin_pic/weixin_search.PNg', MouseOperationEnum.single_click, right_down_10  )
    time.sleep(2)

    right_50_down_10 = {OffsetDirectionEnum.right: 50, OffsetDirectionEnum.down: 10}
    autoGuiUtil.mapping_by_cv2('../../file/weixin_pic/weixin_search_detail.PNg', MouseOperationEnum.single_click,
                               right_50_down_10)

    time.sleep(2)
    pyautogui.typewrite("liutao")
    pyautogui.press("enter")
    pyautogui.press("enter")

    time.sleep(2)

    autoGuiUtil.mapping_by_cv2('../../file/weixin_pic/tao_name.PNg', MouseOperationEnum.single_click,
                               right_50_down_10)

    time.sleep(2)
    left_100_down_10 = {OffsetDirectionEnum.left: 100, OffsetDirectionEnum.down: 10}
    autoGuiUtil.mapping_by_cv2('../../file/weixin_pic/message_text.PNg', MouseOperationEnum.single_click,
                               left_100_down_10)
    pyautogui.typewrite("taozong, ni ming tian mei shi ma")
    pyautogui.press("enter")
    pyautogui.press("enter")

    time.sleep(2)
    autoGuiUtil.mapping_by_cv2('../../file/weixin_pic/send_button.PNg', MouseOperationEnum.single_click,
                               right_50_down_10)

    end_time = datetime.now()
    print("耗时：" + str((end_time - start_time).seconds) + 's ' + str((end_time - start_time).microseconds))