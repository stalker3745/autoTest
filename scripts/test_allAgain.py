import jsonpath
import pytest

from baw import project
from caw import fileRead


class TestAll:
    @pytest.fixture(params=fileRead.read_yaml("/data_case/all.yaml"))
    def project_Resources(self,request):
        return request.param

# �üо�д��¼��������ÿ����������֮ǰ�����¼
    @pytest.fixture(autouse=True)
    def login(self,br,project_Resources):
        r=br.post(url=project_Resources["url"],json=project_Resources["logindata"])
        return r

# project.py���cs��Ӧproject_Resources
# project.py���headers��ӦgetHeaders
    # �鿴���е���Ŀ
    def test_findAll_project(self,url,br,getHeaders,project_Resources):
        # ���Ǹ��ֳɵĽӿڣ��鿴�û��б��õ�
        r=project.listAllProjectByCondition(url,getHeaders,br,project_Resources['listAllProjectByCondition'])
        # ʹ�� JSONPath ��ȡ JSON �����е� message �� code �ֶ�
        # message=jsonpath.parse('$.message')
        # code=jsonpath.parse('$.code')
        # message_match=message.find(r.json())
        # code_match=code.find(r.json())
        message_match = jsonpath.jsonpath(r.json(), "$.message")
        code_match = jsonpath.jsonpath(r.json(), "$.code")
        assert str(message_match[0])==str(project_Resources['exp']['message'])
        assert str(code_match[0])==str(project_Resources['exp']['code'])

    def test_findAllUser_project(self,url,br,getHeaders,project_Resources):
        # ���Ǹ��ֳɵĽӿڣ��鿴�û��б��õ�
        print(project_Resources['getActivityLogByCreateId'])
        r=project.getActivityLogByCreateId(url,getHeaders,br,project_Resources['getActivityLogByCreateId'])
        assert str(r.json()['message'])==str(project_Resources['exp']['message'])
        assert str(r.json()['code'])==str(project_Resources['exp']['code'])