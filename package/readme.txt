no module named 'ppocr.data'
删除系统C盘——用户中.paddle相关文件夹，清除旧版本paddlehub
DLL load failed while importing _remap: 找不到指定的模块
先import paddlehub
编码错误
注释headers中的'accept-encoding'


测试环境：
Package            Version
------------------ ---------
appdirs            1.4.4
astor              0.8.1
Babel              2.9.0
bce-python-sdk     0.8.53
certifi            2020.12.5
cfgv               3.2.0
chardet            4.0.0
click              7.1.2
colorama           0.4.4
colorlog           4.7.2
cycler             0.10.0
decorator          4.4.2
distlib            0.3.1
easydict           1.9
filelock           3.0.12
flake8             3.8.4
Flask              1.1.2
Flask-Babel        2.0.0
future             0.18.2
gast               0.3.3
gitdb              4.0.5
GitPython          3.1.13
h5py               3.1.0
identify           1.5.13
idna               2.10
imageio            2.9.0
imgaug             0.4.0
itsdangerous       1.1.0
jieba              0.42.1
Jinja2             2.11.3
joblib             1.0.1
kiwisolver         1.3.1
lmdb               1.1.1
MarkupSafe         1.1.1
matplotlib         3.3.4
mccabe             0.6.1
networkx           2.5
nodeenv            1.5.0
numpy              1.19.3
opencv-python      4.2.0.32
packaging          20.9
paddlehub          2.0.0
paddlenlp          2.0.0rc1
paddleocr          2.0.2
paddlepaddle       2.0.0
Pillow             8.1.0
pip                19.2.3
pre-commit         2.10.1
protobuf           3.14.0
pyclipper          1.2.1
pycodestyle        2.6.0
pycryptodome       3.10.1
pyflakes           2.2.0
pyparsing          2.4.7
python-dateutil    2.8.1
python-Levenshtein 0.12.2
pytz               2021.1
PyWavelets         1.1.1
PyYAML             5.4.1
pyzmq              22.0.2
rarfile            4.0
requests           2.25.1
scikit-image       0.18.1
scikit-learn       0.24.1
scipy              1.6.0
seqeval            1.2.2
setuptools         41.2.0
Shapely            1.7.1
shellcheck-py      0.7.1.1
six                1.15.0
smmap              3.0.5
threadpoolctl      2.1.0
tifffile           2021.2.1
toml               0.10.2
tqdm               4.56.1
urllib3            1.26.3
virtualenv         20.4.2
visualdl           2.1.1
Werkzeug           1.0.1


WEBAPP环境：
Package         Version
--------------- ----------
appdirs         1.4.4
asgiref         3.3.1
astor           0.8.1
Babel           2.9.0
bce-python-sdk  0.8.53
beautifulsoup4  4.9.3
certifi         2020.12.5
cfgv            3.2.0
chardet         4.0.0
click           7.1.2
cma             3.0.3
colorlog        4.7.2
cycler          0.10.0
decorator       4.4.2
distlib         0.3.1
Django          3.1.6
Faker           6.1.1
filelock        3.0.12
flake8          3.8.4
Flask           1.1.2
Flask-Babel     2.0.0
funcsigs        1.0.2
future          0.18.2
gast            0.3.3
graphviz        0.16
gunicorn        20.0.4
identify        1.5.13
idna            2.10
imageio         2.9.0
imgaug          0.4.0
itsdangerous    1.1.0
Jinja2          2.11.3
joblib          1.0.1
kiwisolver      1.3.1
lmdb            1.1.1
lxml            4.6.2
MarkupSafe      1.1.1
matplotlib      3.3.4
mccabe          0.6.1
mysqlclient     2.0.3
networkx        2.5
nltk            3.5
nodeenv         1.5.0
numpy           1.20.1
objgraph        3.5.0
opencv-python   4.2.0.32
paddlehub       1.8.1
paddleocr       1.1.1
paddlepaddle    1.8.5
pandas          1.2.2
pathlib         1.0.1
Pillow          8.1.0
pip             21.0.1
pre-commit      2.10.1
prettytable     2.0.0
protobuf        3.14.0
pyclipper       1.2.1
pycodestyle     2.6.0
pycryptodome    3.10.1
pyflakes        2.2.0
pyparsing       2.4.7
python-dateutil 2.8.1
pytz            2021.1
PyWavelets      1.1.1
PyYAML          5.4.1
rarfile         4.0
regex           2020.11.13
requests        2.25.1
scikit-image    0.18.1
scipy           1.6.0
selenium        3.141.0
sentencepiece   0.1.95
setuptools      53.0.0
Shapely         1.7.1
shellcheck-py   0.7.1.1
six             1.15.0
soupsieve       2.2
sqlparse        0.4.1
text-unidecode  1.3
tifffile        2021.2.1
toml            0.10.2
tqdm            4.56.2
ua-parser       0.10.0
urllib3         1.26.3
user-agents     2.2.0
virtualenv      20.4.2
visualdl        2.1.1
wcwidth         0.2.5
Werkzeug        1.0.1
wheel           0.36.2
yapf            0.26.0


升级python
# 安装
apt update
apt install software-properties-common
# 添加deadsnakes PPA 源
add-apt-repository ppa:deadsnakes/ppa
# 安装python3.8
apt install python3.8
# 查看python3.8位置
which python3.8
/usr/bin/python3.8
# 设置3.8
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
# 查看python3.5位置 
which python3.5
# 设置3.5
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 2
# 配置 python3 默认指向 python3.8
update-alternatives --config python3
There are 2 choices for the alternative python3 (providing /usr/bin/python3).

  Selection    Path                Priority   Status
------------------------------------------------------------
* 0            /usr/bin/python3.5   2         auto mode
  1            /usr/bin/python3.5   2         manual mode
  2            /usr/bin/python3.8   1         manual mode

Press <enter> to keep the current choice[*], or type selection number: 2
# 测试 python 版本
# python3 -V


E:--apt update --fix错误
# 删除软件及其配置文件
apt-get --purge remove <package>
# 删除没用的依赖包
apt-get autoremove <package>



distutils.errors.DistutilsError: Could not find suitable distribution for Requirement.parse('setuptools-scm')
pip install setuptools-scm
pip install --upgrade pip
pip install setuptools -U


No module named apt_pkg
cd /usr/lib/python3/dist-packages
# 当系统python3.6升级到python3.8时
ln -s apt_pkg.cpython-{36m,38m}-x86_64-linux-gnu.so
apt install python3-pip


 #include <Python.h>
                ^
compilation terminated.
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
apt-get install python3.8-dev


OSError: mysql_config not found
apt-get install libmysqlclient-dev


Error importing cv2: 'libSM.so.6: cannot open shared object file: No such file or directory'
apt-get install -y libsm6 libxext6 libxrender-dev