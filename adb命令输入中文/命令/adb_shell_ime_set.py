# coding:utf-8
import os

# IME_S = os.popen('adb shell ime list -s').read()  # 读取所有有输入法
# print(IME_S)
adbKeyboard = "com.android.adbkeyboard/.AdbIME"  # adbKeyboard键盘名
os.system('adb shell ime set com.android.adbkeyboard/.AdbIME')  # 切换输入法

# app_name = os.popen('adb shell pm list packages').read()  # 读取所有的包名
# print(app_name)
adbKeyboard_name = "package:com.android.adbkeyboard"  # adbKeyboard输入法包名
# app_name_info = os.popen('adb shell dumpsys package com.android.adbkeyboard').read()  # 读取包名信息
# print(app_name_info)

adbIme_push = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), "app", "adbkeyboardsrf.apk")  # 安装包路径
# print(adbIme_push)

print()
print()
print()
print()
print()
print()
print("-------------------------------------------------")
print("--                                             --")
print("注意：在输入中文之前，把当前输入法设为adbkeyboard输入法")
print("--                                             --")
print("-------------------------------------------------")
a = "l"
while True:
    app_name = os.popen('adb shell pm list packages').read()  # 读取所有的包名
    if a == "l" or a == "L":
        if adbKeyboard_name in app_name:
            input_text = input("请输入你要输入的字")
            text01 = f"adb shell am broadcast -a ADB_INPUT_TEXT --es msg {input_text}"
            os.system(text01)
            a = input("L.继续 Q.退出")
        else:
            os.system(f'adb install {adbIme_push}')
            print()
            print()
            print()
            print()
            print("-------------------------------------------------")
            print("--                                             --")
            print("在手机设置管理输入法里面，把ADB Keyboard开关打开，在把当前输入法改为 ADB Keyboard 输入法为 ADB Keyboard")
            print("--                                             --")
            print("-------------------------------------------------")
            print()
            print()
            print()
            print()
            input_text = input("在输入框输入字符")
            text01 = f"adb shell am broadcast -a ADB_INPUT_TEXT --es msg {input_text}"
            os.system(text01)
            a = input("L.继续 Q.退出")
    elif a == "q" or a == "Q":
        break
    else:
        a = input("输入有误 L.进入 Q.退出")
