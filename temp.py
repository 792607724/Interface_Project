# coding = utf8
import os

os.path.abspath(".")
"""
    @Project:Interface_Project
    @File:temp.py
    @Author:十二点前要睡觉
    @Date:2021/12/10 15:32
"""
# coding=utf-8
import os


class LogCleaner():
    def __init__(self):
        pass

    def clean_most_logs(self):
        os.system("adb root")
        os.system("adb shell rm -rf /data/logs/logcat.txt.*")
        os.system("adb shell rm -rf /data/logs/dbus.txt.*")
        os.system("adb shell rm -rf /data/tombstones/*")
        os.system("adb shell rm -rf /data/anr/*")
        os.system("adb shell rm -rf /data/system/dropbox/*")

    def clean_all_logs(self):
        self.clean_most_logs()
        os.system("adb shell rm -rf /sdcard/map/gps/*")
        os.system("adb shell rm -rf /sdcard/amapauto8/logs/*")


l_obj = LogCleaner()
print("正在清理所有的旧log...请稍候！")
l_obj.clean_all_logs()
print("所有旧log清理完毕！")

os.system("pause")
