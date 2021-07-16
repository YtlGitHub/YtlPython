import time
import os


now = time.time()
now_time = time.strftime("%Y:%m:%d_%H:%M:%S", time.localtime(now))  # 获取当前时间
print('电脑时间：'+now_time)
cellPhoneTime = os.popen('adb shell date').read()  # 手机当前时间
print("手机时间：" + cellPhoneTime)
devicesSerial = os.popen('adb devices').read().split()[-2]  # 获取序列号
print("设备串口号：" + devicesSerial)
brand = os.popen('adb shell getprop ro.product.brand').read()  # 品牌
print("品牌：" + brand)
marketName = os.popen('adb shell getprop ro.oppo.market.name').read()  # 获取设备名称
print("设备名称：" + marketName)
projectName = os.popen('adb shell getprop ro.separate.soft').read()  # 产品代号
print("产品代号：" + projectName)
deviceName = os.popen('adb shell getprop ro.product.name').read()  # 获取产品型号
print("机型：" + deviceName)
platformVersion = os.popen('adb shell getprop ro.build.version.release').read()  # 获取Android版本号
print("安卓：" + platformVersion)
OS = os.popen("adb shell getprop ro.build.version.opporom").read()  # OS版本
print("OS版本：" + OS)
OTA = os.popen("adb shell getprop ro.build.version.ota").read()  # OTA版本
print("OTA版本：" + OTA)
try:
    IMEI1 = os.popen("adb shell dumpsys engineer --query_indicate_info").read()  # OTA版本
    print("IMEI1：" + IMEI1.split()[11])
    print("GUID：" + IMEI1.split()[17])
    print("Carrier：" + IMEI1.split()[9])
except:
    pass
OTA_ON_OFF = os.popen("adb shell getprop sys.ota.test").read()  # OTA版本
print(f"OTA开关(1为开，0或者空为关)：{OTA_ON_OFF}")
MTK = os.popen("adb shell getprop Build.BRAND").read()  # OTA版本
print(f"MTK或高通：{MTK}")
input("按任意键退出")
