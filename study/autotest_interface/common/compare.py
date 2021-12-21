# coding = utf8
import os

os.path.abspath(".")
"""
    @Project:Interface_Project
    @File:compare.py
    @Author:十二点前要睡觉
    @Date:2021/12/21 10:34
"""

"""
    定义数据比较方法
    1、compare_param是对外的参数比较类
    2、compare_code是关键参数值的比较方法，
    compare_params_complete是参数完整性的比较方法
    3、get_compare_params是获得返回包数据去重后集合的方法
    4、recur_params递归操作方法，辅助去重
"""

import json, os, logging
from study.autotest_interface.common import opmysql
from study.autotest_interface.public import config

# 实例化测试数据库操作类
operation_db = opmysql.OperationDbInterface(password_db="seevision")


class CompareParam(object):

    # 初始化数据
    def __init__(self, params_interface):
        pass

    # 定义关键参数值(code)比较
    def compare_code(self, result_interface):
        pass

    # 定义将接口返回数据中的参数名写入列表中
    def get_compare_params(self, result_interface):
        pass

    # 参数完整性比较方法，
    def compare_params_complete(self, result_interface):
        pass

    # 定义递归方法
    def __recur_params(self, result_interface):
        pass


if __name__ == '__main__':
    pass
