import jsonpath
import pytest

from baw import project
from caw import fileRead


class TestAll:
    @pytest.fixture(params=fileRead.read_yaml("/data_case/all1.yaml"))
    def project_Resources(request):
        return request.param

# 用夹具写登录，这样在每个方法运行之前都会登录
    @pytest.fixture(autouse=True)
    def login(self,project_Resources,br,cs):
        r=br.post(url=project_Resources['url'],json=cs)
        return r

# project.py里的cs对应project_Resources
# project.py里的headers对应getHeaders
    # 查看所有的项目
    def test_findAll_project(self,url,br,getHeaders,project_Resources):
        # 这是个现成的接口，查看用户列表用的
        r=project.listAllProjectByCondition(url,br,getHeaders,project_Resources['listAllProjectByCondition'])
        # 使用 JSONPath 提取 JSON 数据中的 message 和 code 字段
        message=jsonpath.parse('$.message')
        code=jsonpath.parse('$.code')
        message_match=message.find(r.json())
        code_match=code.find(r.json())
        assert str(message_match[0].value)==str(project_Resources['exp']['message'])
        assert str(message_match[0].value)==str(project_Resources['exp']['code'])

    def test_findAllUser_project(self,url,br,getHeaders,project_Resources):
        # 这是个现成的接口，查看用户列表用的
        r=project.getActivityLogByCreateId(url,br,getHeaders,project_Resources['getActivityLogByCreateId'])
        assert str(r.json()['message'])==str(project_Resources['exp']['message'])
        assert str(r.json()['code'])==str(project_Resources['exp']['code'])