mkvirtualenv [py_flask]   创建虚拟环境（python2的）
which python    查看当前虚拟环境目录
deactivate    推出当前虚拟环境
mkvirtualenv -p python3 [py3_flask27]    创建虚拟环境（python3的）
workon [py3_flask27]  进入虚拟环境
workon +2下tab键    查看虚拟环境
rmvirtualenv [py3_flask27]    删除虚拟环境

pip install flask==0.10.1 安装flask
pip freeze  查看当前虚拟环境中有什么东西