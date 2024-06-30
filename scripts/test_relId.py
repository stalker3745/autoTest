# -*- coding: utf-8 -*-
import time
import jsonpath
import pytest
import requests

from baw import project
from caw import fileRead

class TestRelId:
    @pytest.fixture(params=fileRead.read_yaml("/data_case/Project.yaml"))
    def project_data(self, request):
        return request.param


    # 新增项目
    def test_addProject_project(self, project_data, url, br, getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        projectId = jsonpath.jsonpath(r.json(), "$..data")
        projectIds= {
            "projectIds": [r.json()["data"]]
        }
        print("项目创建成功，新创的项目Id为：" + str(projectId))
        time.sleep(5)
        r=project.deleteProject(url, br, getHeaders,projectIds)
        print(r.json())
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])



    # 删除项目
    def test_deleteProject_project(self, project_data, url, br, getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectIds={
            "projectIds":[ r.json()["data"]]
        }
        time.sleep(5)
        r = project.deleteProject(url, br, getHeaders,projectIds)
        print(r.json())
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        print("删除项目成功")

    # 查看当前项目下所有的成员
    def test_getUserIdsByProjectId(self, project_data, url, br, getHeaders):
        getUserIdsByProjectId = {"projectId":"1251505172283424768"}
        r=project.getUserIdsByProjectId(url,br,getHeaders,project_data['getActivityLogByCreateId'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert len(r.json()["data"]) == 8


    # 添加项目任务
    def test_addTask_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        add = project.addProject(url, br, getHeaders, project_data['addProject'])
        data = {
              "taskName": "1",
              "isToBeClaimed": "0",
              "assistantUserIds": [],
              "taskPriority": 2,
              "taskPhaseId": "1242522938167877632",
              "taskType": 1,
              "projectId":  add.json()["data"],
              "parentTaskId": -1
            }
        task=project.addTask(url,br,getHeaders,data)
        assert str(task.json()["code"]) == str(project_data['exp']['code'])
        assert str(task.json()['message']) == str(project_data['exp']['message'])
        projectIds= {
            "projectIds": [add.json()["data"]]
        }
        r=project.deleteProject(url, br, getHeaders,projectIds)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])


    # 项目归档
    def  test_updateDataType_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
        data = {
            "projectId": r1.json()["data"],
            "dataType": 2
        }
        print(data)
        r=project.updateProjectDataType(url,br,getHeaders,data)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print("项目已归档")
        projectIds= {
            "projectIds": [r1.json()["data"]]
        }
        r=project.deleteProject(url, br, getHeaders,projectIds)
        print(r.json())
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

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
        projectIds= {
            "projectIds": [r1.json()["data"]]
        }
        r=project.deleteProject(url, br, getHeaders,projectIds)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])


    # 获取relId
    def test_getUserRelId_project(self, project_data, url, br, getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectId = {
            "projectId": r.json()["data"],
            "projectIds": [r.json()["data"]]
        }
        r = project.getUserIdsByProjectId(url, br, getHeaders, projectId)
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        relId = jsonpath.jsonpath(r.json(), "$..relId")
        assert len(relId) != 0
        print("新增用户的relId为：" + str(relId))
        r=project.deleteProject(url, br, getHeaders,projectId)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 增加项目成员
    def test_addpeople_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r2 = project.addProject(url, br, getHeaders, project_data['addProject'])
        assert str(r2.json()["code"]) == str(project_data['exp']['code'])
        assert str(r2.json()['message']) == str(project_data['exp']['message'])
        user= {"page":1,"pageSize":0,"queryIden":0,"accountStatus":1,"userDuty":1}
        r1= project.listCompanyUserPage(url, br, getHeaders, user)
        data = {
            "projectId": r2.json()["data"],
            "userIdList": jsonpath.jsonpath(r1.json(),"$..userId"),
            "roleIdList": jsonpath.jsonpath(r1.json(),"$..userId"),
            "projectIds": [r2.json()["data"]]
        }
        r = project.changeProjectResourc(url,br,getHeaders,data)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        r=project.deleteProject(url, br, getHeaders,data)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 移除项目成员
    def test_deleteResourc_project(self, project_data, url, br, getHeaders):
        time.sleep(5)
        r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
        # 添加项目成员
        user = {"page": 1, "pageSize": 0, "queryIden": 0, "accountStatus": 1, "userDuty": 1}
        r2 = project.listCompanyUserPage(url, br, getHeaders, user)
        projectId = {
            "projectId": r1.json()["data"],
            "projectIds": [r1.json()["data"]]
        }
        data1 = {
            "projectId": r1.json()["data"],
            "userIdList": jsonpath.jsonpath(r2.json(), "$..userId"),
            "roleIdList": jsonpath.jsonpath(r2.json(), "$..userId"),
            "projectIds": [r1.json()["data"]]
        }
        project.changeProjectResourc(url, br, getHeaders, data1)
        data2 = {
            "isManager": "false",
            "projectId": r1.json()["data"],
            "withRole": "true"
        }
        r3=project.getUserIdsByProjectId(url, br, getHeaders, data2)
        relId=r3.json()['data'][0]['relId']
        print("relId="+relId)
        data3 = {
            "relId": relId,
            "projectId": r1.json()["data"]
        }
        r4=project.deleteProjectResource(url, br, getHeaders,data3)
        assert str(r4.json()["code"]) == str(project_data['exp']['code'])
        assert str(r4.json()['message']) == str(project_data['exp']['message'])
        project.deleteProject(url, br, getHeaders,projectId)
        assert str(r4.json()["code"]) == str(project_data['exp']['code'])
        assert str(r4.json()['message']) == str(project_data['exp']['message'])

    # 将项目从回收站里恢复
    def  test_deleteclean_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r2 = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectId = {
            "projectId": r2.json()["data"],
            "projectIds": [r2.json()["data"]]
        }
        data = {
            "dataType": 1,
            "projectId": r2.json()["data"]
        }
        r = project.updateProjectDataType(url, br, getHeaders, data)
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        data = {
            "dataType": 3,
            "projectId": r2.json()["data"]
        }
        r = project.updateProjectDataType(url, br, getHeaders, data)
        print(r.json())
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print("删除已从回收站内恢复")
        r=project.deleteProject(url, br, getHeaders,projectId)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 创建项目模板
    def test_copyByProjectId_project(self, project_data, url, br, getHeaders):
        time.sleep(5)
        r2 = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectId = {
            "projectId": r2.json()["data"],
        }
        r = project.copeProjectByProjectId(url,br,getHeaders,projectId)
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print("项目模板已创建成功")
        projectIds= {
            "projectIds": [r2.json()["data"],r.json()["data"]]
        }
        r=project.deleteProject(url, br, getHeaders,projectIds)
        print(r.json())
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 删除项目模板
    def test_deleteCopy_project(self,project_data, url, br, getHeaders):
        time.sleep(5)
        r2 = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectId = {
            "projectId": r2.json()["data"],
        }
        r=project.copeProjectByProjectId(url, br, getHeaders, projectId)
        project.deletecopyProject(url,br,getHeaders,projectId)
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print("项目模板已删除成功")
        projectIds= {
            "projectIds": [r2.json()["data"],r.json()["data"]]
        }
        r=project.deleteProject(url, br, getHeaders,projectIds)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 复制项目模板
    def test_copyProjectTemplate_project(self,project_data, url, br, getHeaders):
        time.sleep(5)
        r = project.addProject(url, br, getHeaders, project_data['addProject'])
        data = {
            "projectId": r.json()["data"],
            "copyType": 2,
            "projectName": "test1copy",
        }
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        r1=project.copeProjectByProjectId(url, br, getHeaders, data)
        assert str(r1.json()["code"]) == str(project_data['exp']['code'])
        assert str(r1.json()['message']) == str(project_data['exp']['message'])
        r2=project.copyProjectTemplate(url, br, getHeaders, data)
        assert str(r2.json()['code']) == str(project_data['exp']['code'])
        assert str(r2.json()['message']) == str(project_data['exp']['message'])
        print("项目模板已复制成功")
        projectIds= {
            "projectIds": [r.json()["data"],r1.json()["data"],r2.json()["data"]]
        }
        r=project.deleteProject(url, br, getHeaders,projectIds)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print("删除成功")

    # 查看当前项目下所有成员
    def test_getUserIdsByProjectId_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        # 新增项目
        r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
        user = {"page": 1,
                "pageSize": 0,
                "queryIden": 0,
                "accountStatus": 1,
                "userDuty": 1}
        r2 = project.listCompanyUserPage(url, br, getHeaders, user)
        assert str(r2.json()["code"]) == str(project_data['exp']['code'])
        assert str(r2.json()['message']) == str(project_data['exp']['message'])
        data = {
            "isAll": "false",
            "projectId": r1.json()["data"],
            "userIdList": jsonpath.jsonpath(r2.json(), "$..userId"),
            "projectIds": [r1.json()["data"]]
        }
        r3 = project.changeProjectResourc(url, br, getHeaders, data)
        assert str(r3.json()["code"]) == str(project_data['exp']['code'])
        assert str(r3.json()['message']) == str(project_data['exp']['message'])
        r=project.getUserIdsByProjectId(url,br,getHeaders,data)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert len( r.json()["data"]) != 0
        r = project.deleteProject(url, br, getHeaders, data)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 查看公司下的成员未激活员工
    def test_listCompanyUserPage_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        listCompanyUserPage={
            "companyId": getHeaders["User-Company"],
            "accountStatus": 1
        }
        r=project.listCompanyUserPage(url, br, getHeaders, listCompanyUserPage)
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        assert r.json()["data"]['totalNumber'] > 2

    # 查看公司部门
    def test_listDept_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r=project.listDept(url, br, getHeaders, project_data['addProject'])
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 更改项目阶段为规划阶段
    def test_updateProjectPahseParams_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
        data = {
                "phaseId": "1242522938167877633",
                "projectId": r1.json()["data"]
        }
        r=project.updateProjectPahseParams(url, br, getHeaders, data)
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print("项目阶段已更改为规划阶段")
        projectIds = {
            "projectIds": [r1.json()["data"]]
        }
        r = project.deleteProject(url, br, getHeaders, projectIds)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 开启阶段更新自动化
    def tets_turnonProjectPahseParams_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
        data = {
                "isAutoPhase": True,
                "projectId": r1.json()["data"]
        }
        r=project.updateProjectPahseParams(url, br, getHeaders, data)
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        print(" 已开启阶段更新自动化")
        projectIds = {
            "projectIds": [r1.json()["data"], r.json()["data"]]
        }
        r = project.deleteProject(url, br, getHeaders, projectIds)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 展示阶段列表
    def test_getProjectPahseScheduleList_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectId = {
            "projectId": r1.json()["data"]
        }
        r=project.getProjectPahseScheduleList(url, br, getHeaders, projectId)
        assert str(r.json()['code']) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        projectIds = {
            "projectIds": [r1.json()["data"]]
        }
        r = project.deleteProject(url, br, getHeaders, projectIds)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 查看所有的任务和子任务
    def test_listTreeTask_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r=project.addProject(url, br, getHeaders, project_data['addProject'])
        projectId = {
            "projectId": r.json()["data"],
            "projectIds": [r.json()["data"]]
        }
        data = {
            "taskName": "1",
            "isToBeClaimed": "0",
            "assistantUserIds": [],
            "taskPriority": 2,
            "taskPhaseId": "1242522938167877632",
            "taskType": 1,
            "projectId": r.json()["data"],
            "parentTaskId": -1
        }
        # 添加任务
        project.addTask(url, br, getHeaders, data)
        r=project.listTreeTask(url, br, getHeaders, projectId)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])
        time.sleep(5)
        # 删除项目
        print(projectId)
        r = project.deleteProject(url, br, getHeaders, projectId)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 添加子任务
    def test_addTaskZi_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
        projectId = {
                "projectId": r1.json()["data"],
                "projectIds": [r1.json()["data"]]
            }
        data1 = {
            "taskName": "1",
            "isToBeClaimed": "0",
            "taskPriority": 2,
            "taskPhaseId": "1242522938167877632",
            "taskType": 1,
            "projectId": r1.json()["data"],
            "parentTaskId": -1
        }
        project.addTask(url, br, getHeaders, data1)
        # 取到tasklist的响应值
        r2=project.listTreeTask(url, br, getHeaders,projectId)
        time.sleep(5)
        # 查看list的长度
        print("data里的list长度是",len(r2.json()['data']['list']))
        # 提取parentTaskId
        parentTaskId = r2.json()["data"]["list"][0]["parentTaskId"]
        data2 = {
            "projectId": r1.json()["data"],
            "parentTaskId": parentTaskId,
            "taskName": "test1",
            "taskPriority": "2",
            "taskType": 1,
            "isToBeClaimed": 0
        }
        time.sleep(5)
        r3 = project.addTask(url, br, getHeaders, data2)
        assert str(r3.json()["code"]) == str(project_data['exp']['code'])
        assert str(r3.json()['message']) == str(project_data['exp']['message'])
        # 删除项目
        r = project.deleteProject(url, br, getHeaders, projectId)
        assert str(r.json()["code"]) == str(project_data['exp']['code'])
        assert str(r.json()['message']) == str(project_data['exp']['message'])

    # 添加任务站点
    def test_addProjectSite_project(self,project_data,url,br,getHeaders):
        time.sleep(5)
        r1 = project.addProject(url, br, getHeaders, project_data['addProject'])
        # 获取公司Id
        projectId = {
            "projectId": r1.json()["data"]
        }
        r4 = requests.post(url=url+"/newProject/getProjectById", headers=getHeaders, json=projectId)
        data = {
              "companyId": r4.json()["data"]["companyId"],
              "siteName": "Test1",
              "siteType": "",
              "addressCode": "",
              "detailedAddress": "",
              "longitudeAndLatitude": "",
              "customerContact": "",
              "customerPhone": "",
              "siteNumber": "",
              "isCommon": "",
              "isDeleted": "",
              "gmtCreated": "",
              "gmtModified": "",
              "modifier": "",
              "projectId": r1.json()["data"]
        }
        r2=project.addProjectSite(url, br, getHeaders, data)
        print(r2.json())
        print("站点已创建成功")
        assert str(r2.json()["code"]) == str(project_data['exp']['code'])
        assert str(r2.json()['message']) == str(project_data['exp']['message'])
        r3=project.deleteProject(url,br,getHeaders,projectId)
        assert str(r3.json()["code"]) == str(project_data['exp']['code'])
        assert str(r3.json()['message']) == str(project_data['exp']['message'])
        print("项目已删除")

