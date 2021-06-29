# [uiautomator2使用教程](https://www.cnblogs.com/Appleli/p/11413229.html)(https://www.jb51.net/article/205942.htm)
文章参考：https://vic.kim/2019/05/20/UIAutomator2%E7%9A%84%E4%BD%BF%E7%94%A8/

一、要求

python 3.6+

android 4.4+

二、介绍

uiautomator2 是一个可以使用Python对Android设备进行UI自动化的库。其底层基于Google uiautomator，Google提供的uiautomator库可以获取屏幕上任意一个APP的任意一个控件属性，并对其进行任意操作。

三、地址

GitHub地址：https://github.com/openatx/uiautomator2

or https://github.com/openatx/uiautomator2/blob/master/README.md

 

四、安装

**1、安装uiautomator2**

pip install --pre uiautomator2

pip install pillow

 

**2、初始化**

部署相关的守护进程。

电脑连接上一个手机或多个手机, 确保adb已经添加到环境变量中，执行下面的命令会自动安装本库所需要的设备端程序：uiautomator-server 、atx-agent、openstf/minicap、openstf/minitouch

python -m uiautomator2 init

安装完成，设备上会多一个uiautomator的应用。

 

配置手机设备参数：

有两种方法，一种是通过WIFI，另一种是通过USB数据线将手机链接电脑。

WiFi连接更方便一点，需要保持PC和手机使用的一个WIFI，查看手机连接WIFI的IP地址。

 

**3、测试**

import uiautomator2 as u2

d = u2.connect('127.0.0.1::6555')

print(d.info) 

打印结果：

{'currentPackageName': 'com.android.launcher', 'displayHeight': 1280, 'displayRotation': 1, 'displaySizeDpX': 360, 'displaySizeDpY': 640, 'displayWidth': 720, 'productName': 'DUK-AL20', 'screenOn': True, 'sdkInt': 23, 'naturalOrientation': False}

五、元素定位

## **1、查看app控件**

（1）、安装：

```
pip install --pre --upgrade weditor
（2）、使用
python -m weditor
（3）、工具打开 
默认会通过浏览器打开页面：http://atx.open.netease.com/
（4）工具的操作步骤
选择android、输入手机或者模拟器的ip+端口，点击connect
dump hierarchy是用来刷新页面的
鼠标点击想要的元素，就可以查看他们的控件了
```

## **`2、主要语法`**

```python
 
（1）启动app
d.app_start("com.addcn.android.house591")
（2）关闭app
cls.d.app_stop("com.addcn.android.house591")
（3）ResourceId定位
cls.d(resourceId="com.addcn.android.house591:id/ad_banner").click()
（4）Text定位
d(text="精选").click()
（5）Description定位
d(description="..").click()
（6）ClassName定位
d(className="android.widget.TextView").click()
（7）xpath定位
d.xpath("//*[@content-desc='分享']").click()
```

## 3、其他操作

（1）#组默认元素等待超时（秒）
d.wait_timeout = 20.0  #默认20
（2）元素拖拽
（3）开关点击

- `d(A).left(B), selects B on the left side of A.`

- `d(A).right(B), selects B on the right side of A.`

- `d(A).up(B), selects B above A.`

- `d(A).down(B), selects B under A.`

- ```
	例如：
	#选择“Wi-Fi”右侧的“开关” 
	d(text="Wi‑Fi").right(className="android.widget.Switch").click()
	```

```
（4）获取/统计某个相同条件的数目
d(text="Add new").count
或者
len(d(text="Add new"))
得知数目之后，我们可以通过索引去定位
d(text="Add new")[0]
d(text="Add new")
也可以遍历
for view in d(text="Add new"):
    view.info 
```

```
（5）截图
＃截取屏幕截图并保存到计算机上的文件中，要求Android> = 4.2。
d.screenshot（ “ home.jpg ”） # get PIL.Image格式化图像。当然，你需要首先安装pillow  image = d.screenshot（） # default format =“pillow” 
image.save（ “ home.jpg ”）＃或home.png。目前，只有PNG和JPG支持＃得到OpenCV的格式图像。当然，你需要先安装numpy和cv2 
import cv2
image = d.screenshot（ format = ' opencv'） cv2.imwrite（ ' home.jpg '图像）＃获取原始JPEG数据 imagebin = d.screenshot（格式= '原始'） 打开（ “ some.jpg ”， “ WB ”）.WRITE（imagebin）（6）手势操作
1、单击
d（ text = “ Settings ”）.click()
2、长按
d（ text = “ Settings ”）.long_click（）
3、将对象拖向另一个点或另一个UI对象
＃笔记：拖不能用于为Android <4.3。
＃将UI对象拖动到屏幕点（x，y），0.5秒后 
d（ text = “设置”）.drag_to（x，y， duration = 0.5）
＃将UI对象拖动到另一个（中心位置） UI对象，在0.25秒 
d（ text = “设置”）.drag_to（ text = “ Clock ”， duration = 0.25）4、在屏幕上滑动
# swipe from (sx, sy) to (ex, ey)
d.swipe(sx, sy, ex, ey)
# swipe from (sx, sy) to (ex, ey) with 10 steps
d.swipe(sx, sy, ex, ey, steps=10)
5、在屏幕上拖拽
# drag from (sx, sy) to (ex, ey)
d.drag(sx, sy, ex, ey)
# drag from (sx, sy) to (ex, ey) with 10 steps
d.drag(sx, sy, ex, ey, steps=10)
```

（7）获取对象信息和状态

```
1、d(text="Settings").exists 
＃如果存在则为True，否则为假
or d.exists(text="Settings") # 进一步使用 d(text="Settings").exists(timeout=3) 
\# 等待设置出现在3S，相同.wait（3）
2、检索特定UI对象的信息
d(text="Settings").info
3、获取/设置/清除可编辑字段的文本（例如，EditText小部件）
d(text = “ Settings ”).get_text（）   # get widget text 
d(text = “ Settings ”).set_text（“ My text ... ”）   ＃设置文本 
d(text = “ Settings ”).clear_text（ ）   ＃清除文字
```

（8）系统常用按键

	# press home key
	d.press.home()
	
	# press back key
	d.press.back()
	
	# the normal way to press back key
	d.press("back")----亲测可用
	
	# press keycode 0x07('0') with META ALT(0x02) on
	d.press(0x07, 0x02)
- `home          #手机Home键`
- `back          #手机返回键`
- `left          #对应键盘上的向右键<-`
- `right          #对应键盘上的向右键->`
- `up           #对应键盘上的向上键`
- `down          #对应键盘上的向下键`
- `center          #选中？`
- `menu          #菜单`
- `search          #查找？`
- `enter          #对应键盘上的Enter键`
- `delete`(or `del`)              #对应键盘上的DEL键 用于删除
- `recent`(recent apps)          #任务切换
- `volume_up         #声音向上调整`
- `volume_down        #声音向下调整`
- `volume_mute        #静音按键`
- `camera          #拍照`
- `power          #电源键`

六、断言

try:

​	d(判断条件).click()

​	print("测试成功")

except：

​	print("测试失败")

六、使用经验
1、使用前初始化
python -m uiautomator2 init
2、打开工具

```python
python -m weditor
```

## 4、app操作

#### 添加提示

```python
d.toast.show('')
```

#### 安装app

```python
url = "地址"
d.app_install(url)
```

#### 打开app

```python
print(d.app_current())  #获取当前正在运行的app
```

#### 卸载app

```python
d.app_uninstall(包名)
```

#### 等待程序运行

```python
方法一：pid = d.app_wait('#包名')   #等待应用运行
if not pid:
    print('#包名'+'没有运行')
else:
    print('#包名pid是 %d' % pid)
方法二：d.app_wait('#包名',front = True)  #等待应用前台运行
方法三：d.app_wait('#包名',timeout = 20.0) #最长等待时间20s
```

#### 检查并维持设备端守护进程处于运行状态

```python
d.healthcheck()
```

#### 检测应用程序崩溃

```python
sess = d.session('#包名')  #启动某app
sess.close() #停止某app
sess.restart() #冷启动某app
```

#### app启动

```python
d.app_start('#包名')
d.app_start('包名','活动名')
```

#### 关闭app

```python
d.app_stop('#包名')
```

#### 清除app数据

```python
d.app_clear('#包名')
```

#### 截图

```python
d.screenshot(r'd:\xxx.png')  #在D盘目录下创建一个xxx.png的截图
```

#### 隐式等待

```python
d.implicitly_wait(3)
```

### 5、按键操作

```python
d.screen_on()  #屏幕点亮
d.unlock()   #解锁屏幕
d.screen_off()  #熄屏
d.press("home")  #回到主界面
d.press("back")	 #返回
d.press("left")  #左滑屏
d.press("right")  #右滑屏
d.press("up")	#上滑屏
d.press("down")  #下滑屏
d.press("search") #负一屏搜索
d.press("enter")  #回车键
d.press("delete") #清除app
d.press("power")  #电源键
d.info.get('screenOn') #获取当前屏幕状态
```

### 6、元素定位

##### python -m weditor

```python
text  #根据text文本进入  d(text = '柠檬班').click()
textContains  #包含text文本(模糊定位)  d(textContains = '柠檬班').click()
className，classNameMatches
description,
descriptionContains,
descriptionMatches,
descriptionStartsWith
checkable,checked,clickable,longClickable
scrollable,enabled,focusable,focused,selected
packageName,packageNameMatches
resourceId,resourceIdMatches
index,instance
```

### 7、页面相对位置元素定位

left，左边的元素

right，右边的元素

up，上面的元素

down，下面的元素

```python
my = d(resourceId = '#某个元素')
my.left().click()   #点击某个元素左边的那个元素
```

### 8、app操作

百分比定位

```python
d.click(#百分比)
```

### 9、滑动操作

```python
#原始版
d.swipe(#startx, starty, endx, endy)
d.swipe(#startx, starty, endx, endy，0.5)  #滑动0.5s
#扩展板
d.swipe_ext('left') #手指左滑，4选1  ：left,right,up,down
d.swipe_ext('left',scale=0.9) #默认0.9，滑动距离为屏幕宽度的90%
d.swipe_ext('left'box = (0 , 0, 100, 100)) #在（0， 0） _> (100， 100)这个区域滑动
#先定位元素，再使用元素对象滑动
e = d(text='某一元素')
e.swipe('down',steps=100)
#滑动点击
d.swipe_points([(x0, y0),(x1,y1),(x3,y3)],0.2))
```

#### 10、拖拽

```python
d.drag(sx, sy, ex ,ey)  #从某坐标拖到某坐标
d.drag(sx, sy, ex ,ey， 0.5)  #从某坐标拖到某坐标 滑动0.5s
```

#### 11、触摸&滑动&抬起

```python
d.touch.down(10, 10) #模拟按下
time.sleep(.01)  #down和move之间有延迟，自己控制
d.touch.move(15,15) #模拟滑动
d.touch.up()  #模拟抬起
```

#### 12、打开通知栏和快速设置

```python
d.open_notification() #打开通知栏
d.open_quick_settings() #打开快速设置
```

### 13、输入&清空

```python
#输入
send_keys("#需要输入的内容")
#清空
clear_text()
```

### 14、截图

```python
#直接截图保存在路径
d.screenshot("文件名.png")
#指定截图保存路劲
d.screenshot(r'd:\xxx.png')  #在D盘目录下创建一个xxx.png的截图
```

### 15、元素等待

```python
#设置元素查找等待时间（默认20s）
d.implicitly_wait(10.0)
d(text = 'Settings').click()  #如果这个text元素在10秒钟没有显示，将会报错
#智能等待
d.time_timeout = 30  #设置全局等待时间为30秒（更改默认时间）
d.app_start("#包名",wait = True)   #超时默认20秒
#等待某一个页面加载完成
d.wait_activity()
#等待某一个元素出现
d().wait()
#等待某一个与元素消失
d().wait_gone()
#等待元素是否存在
d().exists()
#等待点击，设置隐式等待
click,clear_text()
.click(timeout = 50) #设置单独点击时间
d().set_text(timeout = 50)  #设置输入文本
#判断一个元素是否存在
eg:
    login_btn = d(resourecId = "#元素名")
   	 if login_btn.exists():
        #执行
       login_btn.click
```

### 16、断言（预期结果是否等于实际结果的过程）

```python
assert d.toast.get_massage() == "#某个字符串"
```

### 17、pytest中mark标签使用

```python
#在每个def用例上打上标签
eg:
    @pytest.mark.#标签名
    def test_login_empty():
        
if __name__ == '__main__':        
	pytest.main(['-m #标签名'])     
```

#### 18、一个非常有用的代码

```python
with d.watch_context() as ctx:
    ctx.when("立即（下载|更新）").when("取消").click() #当同是出现（立即安装或立即取消） 和取消 按钮的时候，点击取消
    ctx.when("同意").click()
    ctx.when("确定").click()
    #上面三行代码是立即执行的完的，不会有什么等待
    ctx.wait_stable()  #开启弹窗监控，并等待界面稳定（两个弹窗检查周期内没有弹窗代表稳定）
    
    #使用call函数来触发函数回调
    #call支持两个参数，d和el，不区分参数位置，可以不传参，如果传参变量名不能写错
    #e.g：当有元素匹配仲夏之夜，点击返回按钮
    ctx.when('仲夏之夜').call(lambda d: d.press("back"))
    ctx.when('确定').call(lambda el: el.click())
	
    #其他操作
#为了方便也可以使用代码中默认的弹窗监控逻辑
#下面是目前内置的默认逻辑
with d.watch_context(builtin = True) as ctx:
    #在已有的基础上增加
    ctx.when('@tb:id/jview_view').when('//*[@content-desc = '图片']').click()
    
另一种写法
	ctx = d.watch_context()
    ctx.when('设置').click()
    ctx.wait_stable() #等待界面不再有弹窗了
    ctx.close()

注册监控
#常用写法，注册匿名监控
d.watcher.when('安装').click()
#注册名为ANR的监控，当出现ANR和Force Close时，点击Force Close
d.watcher('ANR').when(xpath='ANR').when('Force Close').click()

#其他回调例子
d.watch.when('抢红包').press('back')
d.watch.when("//*[text = 'Out of memory']").call(lambda d: d.shell('am force-stop com.im.qq'))

#回调说明
def click_callback(d: u2.Device):
    d.xpath("确定").click() #在回调中调用不会再次出发watcher
d.xpath("继续").click()  #使用d.xpath检查元素的时候，会出发watcher(目前最多出发5次)

#监控操作
#移除ANR的监控
d.wathder.remove("ANR")

#移除所有的监控
d.watcher.remove()

#开始后台监控
d.watcher.start()
d.watcher.start(2.0)  #默认监控间隔2.0秒

#强制运行所有监控
d.watcher.run()

#停止监控
d.watcher.stop()

#停止并移除所有的监控，常用于初始化
d.watcher.reset()
```

#### 18、输入法

```python
d.set_fastinput_ime(True) #切换成FastInputIME输入法
d.send_keys("你好123abcEFG") #adb广播输入
d.clear_text() #清楚输入框所有内容
d.set_fastinput_ime(False)  #切换成正常的输入法
d.send_action('search') #模拟输入法的搜索
```

#### 19、Toast

```python
#Show Toast
d.toast.show('Hello world')
d.toast.show('Hello world',1.0)   #显示为1.0秒，默认为1.0

#Get Toast
d.toast.get_message(5.0,10.0,"defult message")

#clear cached toast
d.toast.reset()
```

#### 20、视频录制

```python
第一步：安装依赖包
pip3 install -U "uiautomator2[image]"
第二步：使用方法
d.screenrecord('output.mp4')
time.sleep(10)
d.screenrecord.stop()  #停止录制后，output.mp4 文件才能打开
```

#### 21、图像适配

```python
第一步：安装依赖包
pip3 install -U "uiautomator2[image]"
第二步：使用方法
imdata = "target.png"
d.image.match(imdata)
#匹配待查找的图片，立刻返回一个结果
#返回一个dice，eg:{"similarity":0.9,"point":[200,300]}
d.image.click(imdata, timeout=20.0)  #在20s的时间内调用match轮询查找图片，执行点击操作
```

#### 22、停止UIAutomator

```python
d.service("uiautomator").stop()
```
