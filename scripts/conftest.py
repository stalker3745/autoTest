'''
脚本层通用的一些前置/后置
使用时候不用import。
pytest是根据conftest文件名字来找的。
'''
import requests

from baw import member
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

@pytest.fixture(scope='module')
def getuserheaders():
    # headers = {"Content-Type": "application/json;charset=utf8"}
    # url = "http://user-sit.zdsztech.com/employee-web-application/account/mixLogin"
    # data = {"account": "15529310001", "password": "dog7jCEMgBCy02XUcrsv4w==", "language": "CN"}  # 配置用户登录的账号
    # r = requests.post(url=url, headers=headers, json=data)
    url=fileRead.read_ini("/data_env/env.ini", "url")+"/account/mixLogin"
    r = requests.post(url=url, json= fileRead.read_yaml("/data_case/loginmax.yaml")["logindata"])
    headers = {
        'Authorization': r.json()["data"]["jwtToken"],
        'User-Company': r.json()["data"]["companyId"]}
    return headers



