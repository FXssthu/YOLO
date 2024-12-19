# YOLO 
YOLO入门教程：如何训练自己的数据集

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

# 其他问题:pip缓存清除
```
# Extend:深度学习环境配置！
GPU cuda pytorch torch anaconda 

conda TensorFlow tense pip sudo 

GPU驱动 

相互关系:例：只有NVIDIA的GPU才支持pytorch

# 其他问题解决

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
