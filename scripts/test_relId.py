# -*- coding: utf-8 -*-

import jsonpath
import pytest

from baw import project, account
from caw import fileRead


class TestRelId:
    @pytest.fixture(params=fileRead.read_yaml("/data_case/Project.yaml"))
    def project_data(self, request):
        return request.param

    class_relId =""
    class_projectId=""

    # 新增项目
    def test_addProject_project(self, project_data, url, br, getHeaders):
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        projectId = jsonpath.jsonpath(r.json(), "$..data")
        print("新创的项目Id为："+str(projectId))
        self.class_projectId=projectId
        return self.class_projectId

    # 新增项目成员
    def test_addUserRelId_project(self, project_data, url, br, getHeaders):
        r = project.changeProjectResourc(url, br, getHeaders, project_data['changeProjectResourc'])
        print(r.json())
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 获取relId
    def test_getUserRelId_project(self, project_data, url, br, getHeaders):
        r = project.getUserIdsByProjectId(url, br, getHeaders, project_data['getUserIdsByProjectId'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        relId = jsonpath.jsonpath(r.json(), "$..relId")
        print("新增用户的relId为："+str(relId))
        self.class_relId =relId
        return self.class_relId

    # 移除项目成员
    # def test_deleteResourc_project(self,project_data, url, br,getHeaders):
    #     r = project.deleteProjectResource(url, br, getHeaders, project_data['deleteProjectResource'],self.class_relId)
    #     assert str(r.json()["code"]) == str(project_data['exp']['code'])
    #     assert str(r.json()['message']) == str(project_data['exp']['message'])


    # 查看当前项目下所有的成员
    def test_getUserIdsByProjectId(self, project_data, url, br, getHeaders):
        account.changeCompanyLogin(url,getHeaders,br,project_data['changeCompanyLogin'])
        r=project.getUserIdsByProjectId(url,br,getHeaders,project_data['getUserIdsByProjectId'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 添加项目任务
    def test_addTask_project(self,project_data,url,br,getHeaders):
        r=project.addTask(url,br,getHeaders,project_data['addTask'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 项目归档
    # 存在问题
    # def  test_updateDataType_project(self,project_data,url,br,getHeaders):
    #     r=project.updateProjectDataType(url,br,getHeaders,project_data['updateProjectDataType'],self.class_projectId)
    #     assert str(r.json()["code"]) == str(project_data['exp']['code'])
    #     assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 查看当前项目下所有成员
    # 还未写完
    # def test_getAllUser_project(self,project_data,url,br,getHeaders):
    #     r=project.getProjectList(url,br,getHeaders,project_data['getProjectList'])
    #     assert str(r.json()["code"]) == str(project_data['exp']['code'])
    #     assert str(r.json()['message']) == str(project_data['exp']['message'])