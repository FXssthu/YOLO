# 一、YOLO 
YOLO入门教程：如何训练自己的数据集

## 1.安装anaconda
python包和环境管理工具，类似操作系统界的VMware

和conda又是什么关系:包管理工具:conda、pip、apt分别是什么 

[Anaconda下载官网](https://www.anaconda.com/download)

记得配置anaconda的环境变量，什么是环境变量=为什么要配置环境变量=环境变量有什么作用

```
D:\anaconda3
D:\anaconda3\Scripts
D:\anaconda3\Library\bin
D:\anaconda3\Library\mingw-w64\bin
```
```python
#验证是否安装成功
conda --version
#更详细的信息查询
conda info
```
为了深入了解anaconda的组成，便于分析后续可能遇到的问题，我们决定分析一下conda info的内容

复制下面内容到语言大模型，package cache可能以后分析问题会遇到

```
PS C:\Users\Administrator> conda info

     active environment : None     #现有激活的环境
       user config file : C:\Users\Administrator\.condarc
 populated config files : D:\anaconda\.condarc
                          C:\Users\Administrator\.condarc
          conda version : 24.9.2
    conda-build version : 24.9.0
         python version : 3.12.7.final.0
                 solver : libmamba (default)
       virtual packages : __archspec=1=skylake
                          __conda=24.9.2=0
                          __cuda=12.7=0
                          __win=0=0
       base environment : D:\anaconda  (writable)
      conda av data dir : D:\anaconda\etc\conda
  conda av metadata url : None
           channel URLs : https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/noarch
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/win-64
                          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r/noarch
                          https://repo.anaconda.com/pkgs/main/win-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/win-64
                          https://repo.anaconda.com/pkgs/r/noarch
                          https://repo.anaconda.com/pkgs/msys2/win-64
                          https://repo.anaconda.com/pkgs/msys2/noarch
          package cache : D:\anaconda\pkgs
                          C:\Users\Administrator\.conda\pkgs
                          C:\Users\Administrator\AppData\Local\conda\conda\pkgs
       envs directories : D:\anaconda\envs
                          C:\Users\Administrator\.conda\envs
                          C:\Users\Administrator\AppData\Local\conda\conda\envs
               platform : win-64
             user-agent : conda/24.9.2 requests/2.32.3 CPython/3.12.7 Windows/11 Windows/10.0.22631 solver/libmamba conda-libmamba-solver/24.9.0 libmambapy/1.5.8 aau/0.4.4 c/. s/. e/.
          administrator : True
             netrc file : None
           offline mode : False       
```

Extesion:命令行之间的区别

powershell和cmd和Anaconda Prompt和Anaconda PowerShell Prompt和Linux->Terminal区别

pip缓存cache的问题，相关关键词:更新和依赖

pip3和pip的区别

conda相关命令

## 2.使用anaconda
```python
#创建名称为:yolov5_env的环境,指定pyhton版本为3.x
conda create -n yolov5_env python=3.x

#激活/进入 创建好的环境
activate yolov5_env

# 安装pytorch 官网查询版本+命令，只有NVIDIA显卡支持pytorch，Intel、AMD等不支持，例如安装cuda12.4

# 下载YOLOv5源码
git clone https://github.com/ultralytics/yolov5.git

# 进入YOLOv5源码，下载所需其他pyhton包
pip install -r requirements

# 其他问题:pip安装、pip缓存清除、pip存在但无法使用pip install
```
# 二、Extend:深度学习环境配置
GPU cuda pytorch torch anaconda 

conda TensorFlow tense pip sudo 

GPU驱动 

相互关系:例：只有NVIDIA的GPU才支持pytorch

# 三、其他问题解决

### 1.conda缓存清除
清除 Anaconda 的缓存可以帮助释放磁盘空间，或解决某些软件包安装问题。以下是清除 Anaconda 缓存的几种方法：

```python
# 清除所有缓存
conda clean -all
# 清除包缓存
conda clean --packages

```

使用以上方法后，您就可以成功清除 Anaconda 的缓存了。

### 2.浏览器可访问但是git clone 屡战屡败？

```
git config --global http.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
git config --global --unset http.proxy
git config --global --unset https.proxy
```
```
git config --global http.sslVerify "true"
git config --global https.sslVerify "true"
```
```
git config --global http.sslVerify "false
git config --global https.sslVerify "false"
```
