@echo off

echo 本机信息:
for /f "delims=" %%t in ('adb shell date') do set curTime=%%t
echo 手机时间：%curTime%

echo.

for /f "delims=" %%t in ('adb shell getprop ro.product.name') do set productName=%%t
echo 1.deviceName = %productName%

for /f "delims=" %%t in ('adb shell getprop ro.build.version.release') do set releaseVer=%%t
echo 2.Android版本 = Android%releaseVer%

adb shell dumpsys activity | findstr mResume

pause