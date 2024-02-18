'''
脚本层通用的一些前置/后置
使用时候不用import。
pytest是根据conftest文件名字来找的。
'''
from caw import fileRead, baseRequests
import pytest



@pytest.fixture(scope='session')
def url():

    return fileRead.read_ini("/data_env/env.ini", "url")


@pytest.fixture(scope='session')
def db_info():
    return eval(fileRead.read_ini("/data_env/env.ini", "db"))

@pytest.fixture(scope='session')
def br():
    return baseRequests.BaseRequests()  # 创建了一个实例
