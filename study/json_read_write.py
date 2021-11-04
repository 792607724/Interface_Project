# encoding=utf8
import os
os.path.abspath(".")
import json

# 写入Json数据到文件
def writeInToJson():
    data = '{"id":1, "name":"Bruce", "age":"18"}'
    with open("./study/data_writeIn.json", "w") as f:
        json.dump(data, f)

# 读取Json数据文件
def readFromJson():
    with open("./study/data_writeIn.json", "r") as f:
        data = json.load(f)
    print(data)

if __name__ == "__main__":
    writeInToJson()
    readFromJson()
