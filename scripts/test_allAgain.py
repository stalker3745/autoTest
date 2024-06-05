import jsonpath
import pytest

from baw import project
from caw import fileRead


class TestAll:
    @pytest.fixture(params=fileRead.read_yaml("/data_case/all1.yaml"))
    def project_Resources(request):
        return request.param

# �üо�д��¼��������ÿ����������֮ǰ�����¼
    @pytest.fixture(autouse=True)
    def login(self,project_Resources,br,cs):
        r=br.post(url=project_Resources['url'],json=cs)
        return r

# project.py���cs��Ӧproject_Resources
# project.py���headers��ӦgetHeaders
    # �鿴���е���Ŀ
    def test_findAll_project(self,url,br,getHeaders,project_Resources):
        # ���Ǹ��ֳɵĽӿڣ��鿴�û��б��õ�
        r=project.listAllProjectByCondition(url,br,getHeaders,project_Resources['listAllProjectByCondition'])
        # ʹ�� JSONPath ��ȡ JSON �����е� message �� code �ֶ�
        message=jsonpath.parse('$.message')
        code=jsonpath.parse('$.code')
        message_match=message.find(r.json())
        code_match=code.find(r.json())
        assert str(message_match[0].value)==str(project_Resources['exp']['message'])
        assert str(message_match[0].value)==str(project_Resources['exp']['code'])

    def test_findAllUser_project(self,url,br,getHeaders,project_Resources):
        # ���Ǹ��ֳɵĽӿڣ��鿴�û��б��õ�
        r=project.getActivityLogByCreateId(url,br,getHeaders,project_Resources['getActivityLogByCreateId'])
        assert str(r.json()['message'])==str(project_Resources['exp']['message'])
        assert str(r.json()['code'])==str(project_Resources['exp']['code'])