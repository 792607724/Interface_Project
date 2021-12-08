# encoding=utf8

import os
os.path.abspath("..")
import json
json_str = '{"id":1, "name":"51zxw", "password":"666"}'
# 将json数据转换成python数据
data = json.loads(json_str)
print(type(json_str))
print(type(data))
print(data)
print(data["id"])
print(data["name"])