import json

import jsonpath
import pytest
from baw import project
from caw import fileRead

#代码逻辑优化

#获取创建项目的数据
@pytest.fixture(params=fileRead.read_yaml("/data_case/addproject.yaml"))
def project_data(request):
    return request.param

#上面读取的数据通过参数传递都下面函数中使用
def test_addproject(url,br,getuserheaders,project_data):
    # 下发创建项目的请求
    r = project.add_project(url, br ,getuserheaders,project_data['addprojectdata'],)
    print(f"项目r：{r}")
    # 校验添加项目的结果
    assert str(r.json()['message']) == str(project_data['exp']['message'])
    assert str(r.json()['code']) == str(project_data['exp']['code'])


def test_addprojectuser(url, br, getuserheaders,project_data):
    # 下发新增员工的请求
    r = project.changeProjectResourc(url, br, getuserheaders, project_data['adduser'])
    print(f"新增员工r：{r}")
    # 校验添加用户的结果
    assert str(r.json()['message']) == str(project_data['exp']['message'])
    assert str(r.json()['code']) == str(project_data['exp']['code'])


# 获取relId
def test_getUserRelId_project(url, br, getuserheaders, project_data):
    # 下发请求
    r1 = project.getUserRelId(url, br, getuserheaders, project_data['getUserRelId'])
    print(f"查询用户ID：{r1}")
    # 校验结果
    assert str(r1.json()["code"]) == str(project_data['exp']['code'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    # 使用jsonpath模块过滤所有具有’‘relId’'属性的对象
    relId_data = jsonpath.jsonpath(r1.json(),"$..relId")
    print(f"获取relId为：{relId_data}")
    return relId_data
