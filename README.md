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
```md
根据您提供的 `conda info` 输出信息，可以分析如下各项内容的含义：

1. **active environment (活动环境)**: `None` 表示当前没有激活任何 Conda 环境。

2. **user config file (用户配置文件)**: `C:\Users\Administrator\.condarc` 是 Conda 用户的配置文件路径。

3. **populated config files (已填充的配置文件)**: 列出了系统中已填充的配置文件，包括用户配置文件和 base Conda 安装目录中的配置文件。

4. **conda version (Conda 版本)**: `24.9.2` 表示当前安装的 Conda 版本。

5. **conda-build version (Conda Build 版本)**: `24.9.0` 是 Conda Build 的版本，通常用于打包和构建软件包。

6. **python version (Python 版本)**: `3.12.7.final.0` 表示当前使用的 Python 版本。

7. **solver (求解器)**: `libmamba (default)` 表示当前使用的依赖关系解决器是 libmamba，这是一个快速的求解器。

8. **virtual packages (虚拟环境包)**: 这部分显示了 Conda 环境中存在的一些虚拟包，包括架构规格、Conda 版本、CUDA 版本和操作系统版本等信息。

9. **base environment (基础环境)**: `D:\anaconda` 是 Conda 的基础环境目录，您可以在这里安装和管理软件包。

10. **conda av data dir (Conda 可用数据目录)**: `D:\anaconda\etc\conda` 指向 Conda 的可用数据文件夹。

11. **conda av metadata url (Conda 可用元数据 URL)**: `None` 表示当前没有设置可用的元数据 URL。

12. **channel URLs (频道 URL)**: 列出了一系列可用的软件包频道，供 Conda 下载和安装软件包。这里的频道使用了 Tsinghua 反向代理和 Anaconda 官方镜像。

13. **package cache (包缓存)**: 列出 Conda 软件包的缓存位置，Conda 会在这些目录中存储下载的软件包，以避免重复下载。

14. **envs directories (环境目录)**: 列出了 Conda 环境的存储位置，您可以在这些地方寻找或管理创建的环境。

15. **platform (平台)**: `win-64` 表示当前的操作系统平台为 Windows 64位。

16. **user-agent (用户代理)**: 描述了当前的 Conda 客户端版本及所用的其他库和环境信息。

17. **administrator (管理员)**: `True` 表示当前用户具有管理员权限，这可能影响一些软件包的安装和管理行为。

18. **netrc file (netrc 文件)**: `None` 表示没有找到 netrc 配置文件，netrc 文件用于存储登录凭据，但在这里未设置任何。

19. **offline mode (离线模式)**: `False` 表示 Conda 并未处于离线模式，可以连接到网络进行软件包的下载和更新。

通过以上信息，您可以更好地理解当前 Conda 环境的配置和状态。
```
Extesion:命令行之间的区别

powershell和cmd和Anaconda Prompt的区别

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
