import jsonpath
import pytest

from baw import project
from caw import fileRead


# class TestAll:
#     @pytest.fixture(params=fileRead.read_yaml("/data_case/all.yaml"))
#     def project_Resources(self,request):
#         return request.param
#
# # �üо�д��¼��������ÿ����������֮ǰ�����¼
#     @pytest.fixture(autouse=True)
#     def login(self,br,project_Resources):
#         r=br.post(url=project_Resources["url"],json=project_Resources["logindata"])
#         return r

# project.py���cs��Ӧproject_Resources
# project.py���headers��ӦgetHeaders
    # �鿴���е���Ŀ
    # ������
    # def test_findAll_project(self,url,br,getHeaders,project_Resources):
    #     r=project.listAllProjectByCondition(url,getHeaders,br,project_Resources['listAllProjectByCondition'])
    #     # ʹ�� JSONPath ��ȡ JSON �����е� message �� code �ֶ�
    #     message_match = jsonpath.jsonpath(r.json(), "$.message")
    #     code_match = jsonpath.jsonpath(r.json(), "$.code")
    #     assert str(message_match[0])==str(project_Resources['exp']['message'])
    #     assert str(code_match[0])==str(project_Resources['exp']['code'])

# ��δ�ҵ������˺ţ��Ժ��
    # def test_findAllUser_project(self,url,br,getHeaders,project_Resources):
    #     # ���Ǹ��ֳɵĽӿڣ��鿴�û��б��õ�
    #     # r=project.getActivityLogByCreateId(url,getHeaders,br,project_Resources['getActivityLogByCreateId'])
    #     # print(project_Resources['getActivityLogByCreateId'])
    #     r=project.listCompanyUserPage(url,getHeaders,br,project_Resources['listCompanyUserPage'])
    #     message_match = jsonpath.jsonpath(r.json(),"$.message")
    #     code_match = jsonpath.jsonpath(r.json(),"$.code")
    #     assert str(message_match[0])==str(project_Resources['exp']['message'])
    #     assert str(code_match[0])==str(project_Resources['exp']['code'])