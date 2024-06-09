import jsonpath
import pytest

from baw import member, project, account
from caw import fileRead


class TestMyClass:
    headers = ""
    @pytest.fixture(params=fileRead.read_yaml("/data_case/all.yaml"))
    def project_data(self, request):
        return request.param

    def setup_method(self, project_data):
        self.r = member.login(project_data[1], project_data[2], project_data[0]['logindata'])
        self.headers = {
            'Lang': "CN",
            'Authorization': self.r.json()["data"]["jwtToken"],
            'User-Company': self.r.json()["data"]["companyId"]
        }
        return self.headers



    # 将项目从回收站里删除
    def test_delete_project2(self, project_data,getHeaders):
        r = project.deleteProject2(project_data[1], project_data[2], self.headers, project_data[0]['deleteProject2'])
        assert str(r.json()["code"]) == str(project_data[0]['exp']['code'])
        assert str(r.json()['message']) == str(project_data[0]['exp']['message'])
    # 归档项目
    def test_updateProjectDataType_project(self, project_data, getHeaders):
        r = project.updateProjectDataType(project_data[1], project_data[2], self.headers,
                                              project_data[0]['updateProjectDataType'])
        assert str(r.json()["code"]) == str(project_data[0]['exp']['code'])
        assert str(r.json()['message']) == str(project_data[0]['exp']['message'])

    # 从回收站恢复项目
    def test_recover_project(self, project_data):
        r = project.recoverProject(project_data[1], project_data[2], self.headers, project_data[0]['recoverProject'])
        assert str(r.json()["code"]) == str(project_data[0]['exp']['code'])
        assert str(r.json()['message']) == str(project_data[0]['exp']['message'])

    @pytest.fixture(params=fileRead.read_yaml("/data_case/project.yaml"))
    def test_getUserRelId_project(self, request):
        return request.param

    # 添加项目
    def test_add_project(self, project_data):
        r = member.login(project_data[1], project_data[2], self.project_data[0]['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r = project.addProject(project_data[1], project_data[2], headers, self.project_data[0]['addProject'])
        assert str(r.json()["code"]) == str(self.project_data[0]['exp']['code'])
        assert str(r.json()['message']) == str(self.project_data[0]['exp']['message'])

#添加任务
    def test_changeResourc_project(self,url, br, getHeaders, project_data):
        r = project.changeProjectResourc(url, br, getHeaders, project_data['changeProjectResourc'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 获取relId
    def test_getUserRelId_project(self,url, br, getHeaders, project_data):
        r = project.getUserIdsByProjectId(url, br, getHeaders, project_data['getUserIdsByProjectId'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        relId = jsonpath.jsonpath(r.json(), "$..relId")
        # print(f"获取relId为：{relId}"
        return relId

    # 移除项目成员
    def test_deleteResourc_project(self,relId, project_data, url, br):
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.deleteProjectResource(url, br, headers, project_data['deleteProjectResource'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 使用项目模板新建项目
    def test_copeByProjectId_project(self,project_data, url, br):
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.copeProjectByProjectId(url, br, headers, project_data['copeProjectByProjectId'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 删除项目模板
    def test_deletecopyProject_project(self,project_data, url, br):
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.deletecopyProject(url, br, headers, project_data['deletecopyProject'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 复制项目模板
    def test_copyProjectTemplate_project(self,project_data, url, br):
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.copyProjectTemplate(url, br, headers, project_data['copyProjectTemplate'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 删除项目
    def test_delete_project(self,project_data, url, br, db_info):
        r = member.login(url, br, project_data['logindata'])
        print(r.json())
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.deleteProject(url, br, headers, project_data['deleteProject'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 添加任务
    def test_addTask_project(self,project_data, url, br):
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.addTask(url, br, headers, project_data['addTask'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 激活已归档的项目
    def test_updateDataType1_project(self,project_data, url, br):
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.updateProjectDataType1(url, br, headers, project_data['updateProjectDataType1'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 将已归档的项目移至回收站
    def test_updateDataType2_project(self,project_data, url, br):
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.updateProjectDataType2(url, br, headers, project_data['updateProjectDataType2'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 添加项目管理阶段中的管理状态
    # def test_changeProjectPahse_project(project_data,url,br):
    #     r = member.login(url, br, project_data['logindata'])
    #     headers = {'Lang': "CN",
    #                'Authorization': r.json()["data"]["jwtToken"],
    #                'User-Company': r.json()["data"]["companyId"]}
    #     r1 = project.changeProjectPahse(url, br, headers, project_data['changeProjectPahse'])
    #     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
    #     assert str(r1.json()['message']) == str(project_data['exp']['message'])

    # 查看当前项目下所有的成员
    def test_getUserIdsByProjectId_project(self,project_data, url, br, db_info):
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        account.changeCompanyLogin(url, headers, br, project_data['changeCompanyLogin'])
        r = member.login(url, br, project_data['logindata'])
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        r1 = project.getUserIdsByProjectId(url, br, headers, project_data['getUserIdsByProjectId'])
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])


if __name__ == '__main__':
    TestMyClass.setup()
