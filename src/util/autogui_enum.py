# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 14:40
# @Author   : XieYao
# @Software : PyCharm

from enum import Enum, unique

@unique
class MouseOperationEnum(Enum):
    single_click = "s"
    double_click = "d"
    right_click = "r"


@unique
class OffsetDirectionEnum(Enum):
    left = "l"
    right = "r"
    up = "u"
    down = "d"