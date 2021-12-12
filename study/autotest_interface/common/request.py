# coding = utf8
import os

os.path.abspath(".")
"""
    @Project:Interface_Project
    @File:request.py
    @Author:十二点前要睡觉
    @Date:2021/12/9 10:39
"""

"""
    封装HTTP请求操作
    1、http_request是主方法，直接供外部调用
    2、__http_get、__http_post是实际底层分类调用的方法
"""
import requests, os, logging
import opmysql
from study.autotest_interface.public import config

# 忽略requests证书警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RequestInterface(object):
    # 定义处理不同类型的请求参数，包含字典、字符串、空值、
    def __new_param(self, param):
        try:
            # 如果接口请求的参数是一个字符串类型的字典，则用eval函数将其还原成字典形式
            if isinstance(param, str) and param.startswith("{"):
                new_param = eval(param)
            # 如果处理请求参数是None，则直接返回一个空字符
            elif param == None:
                new_param = ""
            # 如果是其他情况，则都返回本来的参数
            else:
                new_param = param
        except Exception as ex:
            new_param = ""
            self.log_print(ex, level=logging.DEBUG)
        return new_param

    # POST请求，参数在body中，处理POST类型接口请求的内部方法
    def __http_post(self, interface_url, headerdata, interface_param):
        """
        POST request,param in body, execute the internal method in post type interface
        @param interface_url:   interface address
        @param headerdata:  request head file
        @param interface_param: interface request param
        @return:dictionary type result
        """
        try:
            if interface_url != "":
                temp_interface_param = self.__new_param(interface_param)
                response = requests.post(url=interface_url, headers=headerdata, data=temp_interface_param, verify=False,
                                         timeout=10)
                if response.status_code == 200:
                    # 发起请求和响应到达的时间，单位ms
                    durtime = (response.elapsed.microseconds) / 1000
                    result = {"code": "0000", "message": "成功", "data": response.text}
                else:
                    result = {"code": "2004", "message": "接口返回状态错误", "data": []}
            elif interface_url == "":
                result = {"code": "2002", "message": "接口地址参数为空", "data": []}
            else:
                result = {"code": "2003", "message": "接口地址错误", "data": []}
        except Exception as ex:
            result = {"code": "9999", "message": "系统异常", "data": []}
            self.log_print(ex, logging.DEBUG)
        return result

    # GET请求，参数在接口地址后面，处理GET请求的内部方法
    def __http_get(self, interface_url, headerdata, interface_param):
        """
        GET request, param behind the interface url address, execute the internal method in GET request
        @param interface_url:   interface address
        @param headerdata:  request head file
        @param interface_param: interface request param
        @return: dictionary type result
        """
        try:
            if interface_url != "":
                temp_interface_param = self.__new_param(interface_param)
                if interface_url.endswith("?"):
                    requrl = interface_url + temp_interface_param
                else:
                    requrl = interface_url + "?" + temp_interface_param
                response = requests.get(url=requrl, headers=headerdata, verify=False, timeout=10)
                if response.status_code == 200:
                    durtime = (response.elapsed.microseconds) / 1000
                    result = {"code": "0000", "message": "成功", "data": response.text}
                else:
                    result = {"code": "3004", "message": "接口返回状态错误", "data": []}
            elif interface_url == "":
                result = {"code": "3002", "message": "接口地址参数为空", "data": []}
            else:
                result = {"code": "3003", "message": "接口地址错误", "data": []}
        except Exception as ex:
            result = {"code": "9999", "message": "系统异常", "data": []}
            self.log_print(ex, logging.DEBUG)
        return result

    # 统一处理HTTP请求，也是可被直接调用的方法
    def http_request(self, interface_url, headerdata, interface_param, request_type):
        """
        Execute HTTP request in this method, and the method could be use directly
        @param interface_url:   interface address
        @param headerdata:  request head file
        @param interface_param: interface request param
        @param request_type:    request type
        @return:    dictionary type result
        """
        try:
            if request_type == "get" or request_type == "GET":
                result = self.__http_get(interface_url, headerdata, interface_param)
            elif request_type == "post" or request_type == "POST":
                result = self.__http_post(interface_url, headerdata, interface_param)
            else:
                result = {"code": "1000", "message": "请求类型错误", "data": request_type}
        except Exception as ex:
            result = {"code": "9999", "message": "系统异常", "data": []}
            self.log_print(ex, logging.DEBUG)
        return result

    def log_print(self, e, level=logging.DEBUG):
        """
        log saved statement
        @param e: deliver a exception into for saving log
        @param level: deliver the log's level
        @return:None
        """
        if not os.path.exists(config.src_path + "/log"):
            os.mkdir(config.src_path + "/log")
            print("Create log folder!")
        if e:
            logging.basicConfig(filename=config.src_path + "/log/system_error.log", level=level,
                                format="%(asctime)s_%(filename)s[line:%(lineno)d]_%(levelname)s %(message)s")
            logger = logging.getLogger(__name__)
            logger.exception(e)


if __name__ == '__main__':
    for i in range(10):
        # 实例化HTTP请求类..
        test_interface = RequestInterface()
        test_db = opmysql.OperationDbInterface(host_db="127.0.0.1", user_db="root",
                                               password_db="seevision", name_db="test_interface",
                                               port_db=3306, link_type=0)
        sen_sql = "select exe_mode, url_interface, header_interface, params_interface from case_interface where name_interface='ipSearch' and id=1"
        params_interface = test_db.select_one(sen_sql)
        if params_interface["code"] == "0000":
            url_interface = params_interface["data"]["url_interface"]
            headerdata = eval(params_interface["data"]["header_interface"])
            param_interface = params_interface["data"]["params_interface"]
            type_interface = params_interface["data"]["exe_mode"]
            if url_interface != "" and headerdata != "" and param_interface != "" and type_interface != "":
                result = test_interface.http_request(interface_url=url_interface, headerdata=headerdata,
                                                     interface_param=param_interface, request_type=type_interface)
                if result["code"] == "0000":
                    result_resp = result["data"]
                    # 将结果更新到case_interface表中，网页本身原因，无法正确处理到数据，此处示例即可，数据未处理
                    test_db.op_sql(
                        "UPDATE case_interface SET result_interface='{}' WHERE id=1".format(str(result_resp[29:57])))
                    print("处理HTTP请求成功，返回数据是：{}".format(result_resp[29:57]))
                else:
                    print("处理HTTP请求失败")
            else:
                print("测试用例数据中有空值")
        else:
            print("获取接口测试用例数据失败")

        # response = requests.get(url="https://ip.taobao.com/ipSearch?ipAddr=63.223.108.4", headers={'Host':'ip.taobao.com'}, verify=False, timeout=10)
        # print(response.status_code)
        # print(response.text)
