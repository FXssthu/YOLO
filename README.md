# 一、YOLO 
YOLO入门教程：如何训练自己的数据集

## 安装anaconda:python包和环境管理工具，类似操作系统界的VMware

和conda又是什么关系:包管理工具:conda、pip、apt分别是什么 

[Anaconda下载官网](https://www.anaconda.com/download)

记得配置anaconda的环境变量，什么是环境变量=为什么要配置环境变量=环境变量有什么作用

```
D:\anaconda3
D:\anaconda3\Scripts
D:\anaconda3\Library\bin
D:\anaconda3\Library\mingw-w64\bin
```

pip缓存cache的问题，相关关键词:更新和依赖

pip3和pip的区别

conda相关命令


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

### 浏览器可访问但是git clone 屡战屡败？

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
