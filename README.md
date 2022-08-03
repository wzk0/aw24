# A(auto) W(webm) 2(to) 4(mp4)

> 一个自动转换Ubuntu录屏文件格式的小脚本.

## 原因

虽然Ubuntu现在自带的录屏功能比较快捷好用,但是每次保存下来的格式都是`webm`,一个一个手动用`ffmpeg`太麻烦了.

所以制作了这个脚本,可以在检测到`录屏`文件夹里新增的`webm`文件之后,自动转换为`mp4`.

## 使用

首先

下载脚本:

```
https://raw.githubusercontent.com/wzk0/aw24/main/webm2mp4.py
```

随后将脚本移动到`/home/用户名/Videos/录屏`文件夹(其他语言的话名字会变)

接下来共有几个方法:

### 前台挂起

在`录屏文件所在文件夹`直接打开终端输入`python3 webm2mp4.py`即可,但是期间会输出大量文字,且终端基本上是`只读模式`,也无法关闭此终端.

不过好处是可以随时关闭.

### 后台挂起

在`录屏文件所在文件夹`打开终端输入`nohup python3 webm2mp4.py &`,随后即可回车然后关闭此终端,或在此终端进行其他操作.

若要杀死终端:

* 假如此终端未关闭,输入`jobs -l`即可获取`PID`:

![如图所示](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202208032119834.png)

随后输入`kill -9 PID`即可:

![如图所示](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202208032120655.png)

* 假如此终端已关闭,输入`ps ux | grep python3\ webm2mp4.py`可查看`PID`.

同理,获取后输入`kill -9 PID`即可:

![如图所示](https://ghproxy.com/https://raw.githubusercontent.com/wzk0/photo/main/202208032123589.png)

### 开机自启

打开`/etc/init.d`目录,在此编写一个脚本(`nano webm2mp4`):

```
#!/bin/sh

python3 /home/用户名/Videos/录屏/webm2mp4.py
```

或者:

```
#!/bin/sh

nohup python3 /home/用户名/Videos/录屏/webm2mp4.py &
```

> 记得替换`用户名`和自己的录屏文件夹的`名称`.

## 关于

通过观察,我发现Ubuntu的整个录屏过程如下:

1. 开启录屏;

2. 在录屏文件夹创建一个不停往内写入的webm文件;

3. 录屏结束.

在第二步中,这个未创建完的webm的文件名与录屏结束后保存的文件名是一样的,但是文件在这个过程中是隐藏属性的!(就像.开头的文件一样,不过它并不是.开头的)

无法通过`是否创建了新的webm文件`来判断`是否进行了新的录屏`,于是我想了一种新的方法:

在添加新文件(文件列表发生改变,新增webm文件)时获取其大小,休眠3秒后再获取一遍.

如果这两个文件大小一样,说明录屏结束(3秒这个数字是我测试很多次得出来的最小休眠数);

如果两个文件大小不一样,则说明录屏还在进行;

随后使用`ffmpeg`转换格式,转换完之后删除原来的webm文件.

## 最后

拜拜~