# 一、YOLO 
### YOLO阶段:
1.调用已有模型，实现常见目标检测.

2.准备特定数据集，训练自己的模型(**本文示例yolov5和ultralytics系列的训练**).

3.修改神经网络，加入Transformer，发论文，YOLO+视觉大模型...


### 0.准备数据集
创建一个文件夹并 构建以下目录:
```python
└─data
    ├─images     #标注数据集之前应收集/下载好图片们
    │  ├─train   #训练数据集，不需要标注，文件应为png/jpg/pdf  
    │  └─val     #验证数据集，不需要标注，文件应为png/jpg/pdf
    └─labels     #后续创建好环境，安装labelimg后输出xml文件，再使用py脚本修改格式
    │    ├─train  #监督学习，训练标签，应为txt 
    │    └─val    #验证标签，应为txt
    │
    └─ your_dataset.yaml   #告诉YOLO数据的位置和组成
└─yolov5（后面会下载,若是ultralytics，则没有这个）
```
yaml文件格式如下:
```yaml
train: E:/YOLO/data/images/train  # 训练图像路径，相对路径和绝对路径均可
val: E:/YOLO/data/images/val      # 验证图像路径，推荐绝对路径
nc: 2                             # 类别数量
names: ['dog', 'cat']             # 类别名称,记得顺序和标注时创建的类别顺序相同
```
### 1.安装anaconda（记得添加环境变量）
<!--python包和环境管理工具，类似操作系统界的VMware -->

<!--和conda又是什么关系:包管理工具:conda、pip、apt分别是什么 -->

<!--记得配置anaconda的环境变量，什么是环境变量=为什么要配置环境变量=环境变量有什么作用 -->

[Anaconda下载官网](https://www.anaconda.com/download)


<!--
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
 -->
### 2 使用anaconda
**创建名称为:yolov5_env的环境**
```python
conda create -n yolo_env
```
**激活/进入创建的环境**
```pyhton
conda activate yolo_env
```
**安装标注软件，如已有数据集可跳过，以**
```pyhton
pip install labelImg
```
**启动labelimg，常用快捷键w（创建矩形框）,d（下一张）,a（上一张）,记得设置自动保存**
```pyhton
labelimg 
```
**安装pytorch,官网查询版本+命令，只有NVIDIA显卡支持pytorch，Intel、AMD等不支持，以安装cuda12.4为例**
[pytorch官网](https://pytorch.org/)

有时候网络不好，命令末尾可以加上--timeout 100，记得关梯子下载，否则可能下载失败
```python 
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 --timeout 100
```
### 1.yolov5（ultralytics可跳过）
**下载YOLOv5源码**
```python
git clone https://github.com/ultralytics/yolov5.git
```
**进入YOLOv5源码，下载所需其他pyhton包**
```pyhton
cd yolov5 && pip install -r requirements.txt

```

**训练命令，需要进入yolov5源码目录，参数需要根据实际修改** 

```python
python train.py --img 640 --batch -1 --epochs 50 --data ../data/data.yaml --weights yolov5s.pt --device 0  
```
### 2.ultralytics（yolov5可跳过）
**源码下载（任意目录均可，会下载到对应虚拟环境位置）**
```pyhton
pip install ultralytics # 下载ultralytics源码
```
**或者**
```pyhton
pip install -U ultralytics # 更新ultralytics源码
```
**训练命令，任意目录运行均可，但是生成的best.pt会在该目录下**
```python
yolo task=detect mode=train model=yolov8s.pt data=./data/my_dataset.yaml batch=-1 epochs=100 device=0 name=onlyou
```
**其他问题:pip安装、pip缓存清除、pip存在但无法使用pip install、OPM链接库重复、页面文件过大Error、高级系统设置**

```pyhton

```
# 二、Extend:深度学习环境配置
相关名词和关系解释

GPU cuda pytorch torch anaconda 

conda TensorFlow tenser pip sudo 

GPU驱动 cuda编程 cuda Toolkit cuda核心 nvcc

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
git config --global http.sslVerify "false"
git config --global https.sslVerify "false"
```

### 3.清华源、阿里源...下载设置
