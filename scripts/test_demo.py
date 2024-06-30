# coding:utf-8
import time

import jsonpath
import pytest

from baw import project
from caw import fileRead

class Testdemo:
    @pytest.fixture(params=fileRead.read_yaml("/data_case/demo.yaml"))
    def project_Resources(self,request):
        return request.param

    # 获取创建项目的数据
    @pytest.fixture(params=fileRead.read_yaml("/data_case/addproject.yaml"))
    def project_data(self,request):
        return request.param

    # 用夹具写登录，这样在每个方法运行之前都会登录
#     @pytest.fixture(autouse=True)
#     def login(self,url,br,project_Resources):
#         r=br.post(url=project_Resources["url"],json=project_Resources["logindata"])
#         return r

# project.py里的cs对应project_Resources
# project.py里的headers对应getHeaders
    def test_findAll_project(self,url,br,getHeaders,project_Resources):
        r=project.listProjectByCondition(url,br,getHeaders,project_Resources['listAllProjectByCondition'])
        # 使用 JSONPath 提取 JSON 数据中的 message 和 code 字段
        message_match = jsonpath.jsonpath(r.json(), "$.message")
        code_match = jsonpath.jsonpath(r.json(), "$.code")
        assert str(message_match[0])==str(project_Resources['exp']['message'])
        assert str(code_match[0])==str(project_Resources['exp']['code'])

# # # 还未找到更新账号，稍后改
    def test_findAllUser_project(self,url,br,getHeaders,project_Resources):
        # 这是个现成的接口，查看用户列表用的
        # r=project.getActivityLogByCreateId(url,getHeaders,br,project_Resources['getActivityLogByCreateId'])
        # print(project_Resources['getActivityLogByCreateId'])
        listCompanyUserPage = {
            "companyId": getHeaders["User-Company"],
            "accountStatus": 1
        }
        r=project.listCompanyUserPage(url,br,getHeaders,listCompanyUserPage)
        message_match = jsonpath.jsonpath(r.json(),"$.message")
        code_match = jsonpath.jsonpath(r.json(),"$.code")
        assert str(message_match[0])==str(project_Resources['exp']['message'])
        assert str(code_match[0])==str(project_Resources['exp']['code'])
# #
# #     # 上面读取的数据通过参数传递都下面函数中使用
    def test_addproject(self, url, br, getHeaders, project_data):
        # 下发创建项目的请求
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addprojectdata'], )
        print(f"项目r：{r}")
        # 校验添加项目的结果
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        projectIds = {
            "projectIds": [r.json()["data"]]
        }
        r = project.deleteProject(url, br, getHeaders, projectIds)
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])


    def test_addprojectuser(self, url, br, getHeaders, project_data):
        # 下发新增员工的请求
        r = project.changeProjectResourc(url, br, getHeaders, project_data['adduser'])
        print(f"新增员工r：{r}")
        # 校验添加用户的结果
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])

    # 获取relId
    def test_getUserRelId_project(self, url, br, getHeaders, project_data):
        # 下发请求
        r1 = project.getUserRelId(url, br, getHeaders, project_data['getUserRelId'])
        print(f"查询用户ID：{r1.json()["data"][0]["relId"]}")
        # 校验结果
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])
        # 使用jsonpath模块过滤所有具有’‘relId’'属性的对象
        relId_data = jsonpath.jsonpath(r1.json(), "$..relId")
        print(f"获取relId为：{relId_data}")
        return relId_data
