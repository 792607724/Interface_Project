# coding = utf8

import os

os.path.abspath(".")
import time
import pandas as pd
import json

cur_time = time.strftime("%Y%m%d")


def json_to_excel(json_path, excel_path):
    # df = pd.DataFrame(columns=["number", "voltage"])
    df = pd.DataFrame(columns=["number", "rpm"])
    df.to_excel(excel_path, index=False)
    print("{} excel generate success!".format(excel_path))

    with open(json_path, "r") as json_file:
        json_data = json.load(json_file)
    # voltage_raw_data = json_data["vol"]
    rpm_raw_data = json_data["rpm"]
    df_2 = pd.read_excel(excel_path, header=None, engine="openpyxl")
    all_list = []
    i = 0
    for voltage_item in rpm_raw_data:
        i += 1
        temp_list = []
        temp_list.append(i)
        temp_list.append(voltage_item)
        all_list.append(temp_list)
    ds = pd.DataFrame(all_list)
    df_2 = df_2.append(ds, ignore_index=True)
    df_2.to_excel(excel_path, index=False, header=False)


if __name__ == '__main__':
    # json_path = "./voltage_20211105115538.json"
    json_path = "./rpm_20211105115550.json"

    # excel_path = "./voltage_{}.xlsx".format(cur_time)
    excel_path = "./rpm_{}.xlsx".format(cur_time)
    json_to_excel(json_path, excel_path)
