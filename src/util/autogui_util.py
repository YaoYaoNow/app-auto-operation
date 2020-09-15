# -*- coding: utf-8 -*-
# @Time     : 2020/7/25 17:47
# @Author   : XieYao
# @Software : PyCharm
from datetime import datetime
from time import sleep

import pyautogui as auto
import cv2
import numpy as np
import pyperclip
from PIL import ImageGrab

from util.autogui_enum import OffsetDirectionEnum, MouseOperationEnum


class autoGuiUtil():
    @staticmethod
    def mouse_offset(coordinate, direct, distance):
        if direct == OffsetDirectionEnum.left:
            return coordinate[0] - distance, coordinate[1]
        if direct == OffsetDirectionEnum.right:
            return coordinate[0] + distance, coordinate[1]
        if direct == OffsetDirectionEnum.up:
            return coordinate[0], coordinate[1] - distance
        if direct == OffsetDirectionEnum.down:
            return coordinate[0], coordinate[1] + distance

    @staticmethod
    def mouse_click(point, operation_type):
        if operation_type == MouseOperationEnum.single_click:
            auto.leftClick(point[0], point[1])
        if operation_type == MouseOperationEnum.double_click:
            auto.double_click(point[0], point[1])
        if operation_type == MouseOperationEnum.right_click:
            auto.right_click(point[0], point[1])

    @staticmethod
    def mapping_by_cv2(image, operation=MouseOperationEnum.single_click, offset_dic=None, await_time_second=5):
        """
        根据图片索引到位置，可以指定操作，偏移方向，偏移量。
        :param image:  需要定位到的图片位置
        :param operation: 操作，单击还是双击
        :param offset_dic: 偏移的位置,以dict格式传入
        :param await_time_second: 屏幕识别等待的时间
        :return:
        """
        start_time = datetime.now()
        try_count = 0

        # 当尝试时间内会一直循环找
        while (datetime.now() - start_time).seconds < await_time_second:
            try_count += 1
            print(f"【doing】 '{image}'的 {operation} 操作进行第 {try_count} 次尝试：——————————————————————————————————————")
            im = ImageGrab.grab()
            im.save('../../file/pic/screen.png', 'png')
            # 加载原始RGB图像
            img_rgb = cv2.imread("../../file/pic/screen.png")
            # 创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

            # 加载将要搜索的图像模板
            template = cv2.imread(image, 0)
            # 使用matchTemplate对原始灰度图像和图像模板进行匹配
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            # 设定阈值,0.7应该可以
            threshold = 0.6
            # res大于70%,
            loc = np.where(res >= threshold)
            if len(loc[0]) == 0:
                # 如果loc为空，表示没有从屏幕获取到想要的元素，返回重试，并且等待一段时间
                sleep(0.05)
                continue
            x_image = loc[1][0]  # 图片左上角的x坐标
            y_image = loc[0][0]  # 图片右上角的y坐标
            loc_final = (x_image, y_image)

            # 处理偏移量
            if offset_dic is not None:
                for key in offset_dic:
                    loc_final = autoGuiUtil.mouse_offset(loc_final, key, offset_dic[key])
            # 操作
            autoGuiUtil.mouse_click(loc_final, operation)
            print(f"【成功】最终执行点: {loc_final} ;对 '{image}' 的 {operation} 操作第 {(datetime.now() - start_time).seconds} 秒执行成功！")
            return True
        # 如果走到这里，表示规定时间内没有操作成功
        print(f"【失败】对 '{image}' 的 {operation} 操作在 {await_time_second} 秒内没有成功")
        # cv2.destroyAllWindows()
        return False

    @staticmethod
    def construct_offset(left=0, right=0, up=0, down=0):
        return {OffsetDirectionEnum.left: left
                , OffsetDirectionEnum.right: right
                , OffsetDirectionEnum.up: up
                , OffsetDirectionEnum.down: down}

    @staticmethod
    def text_input(text):
        pyperclip.copy(text)
        auto.hotkey("ctrl", "v")
