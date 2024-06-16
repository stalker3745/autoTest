import jsonpath
import pytest

from baw import project
from caw import fileRead


# class TestAll:
#     @pytest.fixture(params=fileRead.read_yaml("/data_case/all.yaml"))
#     def project_Resources(self,request):
#         return request.param
#
# # 用夹具写登录，这样在每个方法运行之前都会登录
#     @pytest.fixture(autouse=True)
#     def login(self,br,project_Resources):
#         r=br.post(url=project_Resources["url"],json=project_Resources["logindata"])
#         return r

# project.py里的cs对应project_Resources
# project.py里的headers对应getHeaders
    # 查看所有的项目
    # 有问题
    # def test_findAll_project(self,url,br,getHeaders,project_Resources):
    #     r=project.listAllProjectByCondition(url,getHeaders,br,project_Resources['listAllProjectByCondition'])
    #     # 使用 JSONPath 提取 JSON 数据中的 message 和 code 字段
    #     message_match = jsonpath.jsonpath(r.json(), "$.message")
    #     code_match = jsonpath.jsonpath(r.json(), "$.code")
    #     assert str(message_match[0])==str(project_Resources['exp']['message'])
    #     assert str(code_match[0])==str(project_Resources['exp']['code'])

# 还未找到更新账号，稍后改
    # def test_findAllUser_project(self,url,br,getHeaders,project_Resources):
    #     # 这是个现成的接口，查看用户列表用的
    #     # r=project.getActivityLogByCreateId(url,getHeaders,br,project_Resources['getActivityLogByCreateId'])
    #     # print(project_Resources['getActivityLogByCreateId'])
    #     r=project.listCompanyUserPage(url,getHeaders,br,project_Resources['listCompanyUserPage'])
    #     message_match = jsonpath.jsonpath(r.json(),"$.message")
    #     code_match = jsonpath.jsonpath(r.json(),"$.code")
    #     assert str(message_match[0])==str(project_Resources['exp']['message'])
    #     assert str(code_match[0])==str(project_Resources['exp']['code'])