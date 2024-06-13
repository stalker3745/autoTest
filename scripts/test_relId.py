# -*- coding: utf-8 -*-
import time

import jsonpath
import pytest
from baw import project
from caw import fileRead

class TestRelId:
    @pytest.fixture(params=fileRead.read_yaml("/data_case/Project.yaml"))
    def project_data(self, request):
        return request.param


    # 新增项目
    def test_addProject_project(self, project_data, url, br, getHeaders):
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        projectId = jsonpath.jsonpath(r.json(), "$..data")
        print("新创的项目Id为：" + str(projectId))
        self.class_projectId = projectId
        return self.class_projectId

    # 删除项目
    def test_deleteProject_project(self, project_data, url, br, getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectIds={
            "projectIds":[ r.json()["data"]]
        }
        r = project.deleteProject(url, br, getHeaders,projectIds)
        print(r.json())
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        print("删除项目成功")

    # 查看当前项目下所有的成员
    def test_getUserIdsByProjectId(self, project_data, url, br, getHeaders):
        r=project.getUserIdsByProjectId(url,br,getHeaders,project_data['getUserIdsByProjectId'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])


    # 添加项目任务
    def test_addTask_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        data = {
                "taskName": "111",
                "isToBeClaimed": "0",
                "taskPriority": 2,
                "taskPhaseId": "1250502212980097024",
                "taskType": 1,
                "projectId": r.json()['data'],
                "parentTaskId": -1,
            }
        r=project.addTask(url,br,getHeaders,data)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])


    # 项目归档
    def  test_updateDataType_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        data = {
            "projectId": r.json()["data"],
            "dataType": 2
        }
        print(data)
        r=project.updateProjectDataType(url,br,getHeaders,data)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print("项目已归档")

    # 激活已归档的项目
    def test_recoverproject_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r1=project.addProject(url,br,getHeaders,project_data['addProject'])
        data = {
            "projectId": r1.json()["data"],
            "dataType": 2
        }
        project.updateProjectDataType(url,br,getHeaders,data)
        data1 = {
                "dataType": 1,
                "projectId": r1.json()["data"]
            }
        r = project.updateProjectDataType(url, br, getHeaders, data1)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print("归档项目已恢复")


    # 获取relId
    def test_getUserRelId_project(self, project_data, url, br, getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectId = {
            "projectId": r.json()["data"],
        }
        r = project.getUserIdsByProjectId(url, br, getHeaders, projectId)
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        relId = jsonpath.jsonpath(r.json(), "$..relId")
        print("新增用户的relId为：" + str(relId))


    # 增加项目成员
    def test_addpeople_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        user= {"page":1,"pageSize":0,"queryIden":0,"accountStatus":1,"userDuty":1}
        r1= project.listCompanyUserPage(url, br, getHeaders, user)
        projectId = {
            "projectId": r.json()["data"],
            "userIdList": jsonpath.jsonpath(r1.json(),"$..userId"),
            "projectIds": [r.json()["data"]]
        }
        r = project.changeProjectResourc(url,br,getHeaders,projectId)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        project.deletecopyProject(url,br,getHeaders,projectId)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])



    # 移除项目成员
    # def test_deleteResourc_project(self,project_data, url, br,getHeaders):
    #     r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
    #     projectId = {
    #         "projectId": r1.json()["data"]
    #     }
    #     project.changeProjectResourc(url, br, getHeaders, projectId)
    #     r2 = project.getUserIdsByProjectId(url, br, getHeaders, projectId)
    #     data = {
    #             "projectId": r2.json()["data"],
    #             "relId": jsonpath.jsonpath(r2.json(), "$..relId"),
    #     }
    #     r = project.deleteProjectResource(url, br, getHeaders, data)
    #     assert str(r.json()["code"]) == str(project_data['exp']['code'])
    #     assert str(r.json()['message']) == str(project_data['exp']['message'])

        # 查看当前项目下所有成员
        # 还未写完
        # def test_getAllUser_project(self,project_data,url,br,getHeaders):
        #     r=project.getProjectList(url,br,getHeaders,project_data['getProjectList'])
        #     assert str(r.json()["code"]) == str(project_data['exp']['code'])
        #     assert str(r.json()['message']) == str(project_data['exp']['message'])
