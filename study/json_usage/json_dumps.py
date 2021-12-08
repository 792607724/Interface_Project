# encoding=utf8
import os
os.path.abspath("..")
import json
data={"id":1, "name":"51zxw", "password":"666"}
print(type(data))

# 将Python数据转换成Json数据
json_str = json.dumps(data)
print(type(json_str))
print(json_str)
