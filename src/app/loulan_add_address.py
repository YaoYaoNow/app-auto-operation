# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 22:54
# @Author   : XieYao
# @Software : PyCharm
import time

from util.autogui_util import autoGuiUtil
from util.autogui_enum import MouseOperationEnum, OffsetDirectionEnum
import pyautogui

if __name__ == '__main__':
    dir_root = '../../file/loulan_add_address'
    right_10_down_10 = autoGuiUtil.construct_offset(0, 10, 0, 10)
    # 找到楼兰公众号
    # 搜索楼兰
    autoGuiUtil.mapping_by_cv2(dir_root + '/search_in_weixin.PNG'
                               , offset_dic=right_10_down_10
                               , await_time_second=10)
    autoGuiUtil.mapping_by_cv2(dir_root + '/search_in_detail.PNG')
    autoGuiUtil.text_input("楼兰")
    pyautogui.press("enter")

    # 点击楼兰进入楼兰公众号详情
    autoGuiUtil.mapping_by_cv2(dir_root + "/loulan_logo.PNG"
                               , await_time_second=4)
    # 点击进入个人中心
    autoGuiUtil.mapping_by_cv2(dir_root + '/lan_fen_jia_yuan.PNG'
                               , await_time_second=20)
    autoGuiUtil.mapping_by_cv2(dir_root + '/zhuce.PNG')
    autoGuiUtil.mapping_by_cv2(dir_root + '/wo_de_shou_huo_di_zhi.PNG'
                               , await_time_second=20)

    # 新增地址
    autoGuiUtil.mapping_by_cv2(dir_root + '/xin_zeng_di_zhi.PNG'
                               , await_time_second=10)

    # 填写详细地址信息
    # 姓名
    autoGuiUtil.mapping_by_cv2(dir_root + '/detail_name.PNG')
    autoGuiUtil.text_input("****")

    # 选择男士
    autoGuiUtil.mapping_by_cv2(dir_root + '/detail_male.PNG')
    # 手机号码
    autoGuiUtil.mapping_by_cv2(dir_root + '/detail_phone.PNG')
    autoGuiUtil.text_input('***')
    # 收货地址
    autoGuiUtil.mapping_by_cv2(dir_root + '/detail_address.PNG')
    time.sleep(0.5)
    autoGuiUtil.mapping_by_cv2(dir_root + '/detail_address_input.PNG'
                               , offset_dic=autoGuiUtil.construct_offset(0, 250, 0, 10))
    autoGuiUtil.text_input("壹方中心")
    autoGuiUtil.mapping_by_cv2(dir_root + '/detail_address_select.PNG')
    autoGuiUtil.mapping_by_cv2(dir_root + '/detail_door.PNG')
    autoGuiUtil.text_input('3楼15号')
    # 保存
    autoGuiUtil.mapping_by_cv2(dir_root + '/detail_save.PNG')
