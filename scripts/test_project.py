import jsonpath
import  pytest

# 登录的数据
from baw import account
from baw import project
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/Project.yaml"))
def project_data(request):
    return request.param


def test_allProject_project(project_data, url, br, db_info):
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    account.changeCompanyLogin(url, br, headers, project_data['changeCompanyLogin'])
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1=project.listAllProjectByCondition(url,headers, br,project_data['listAllProjectByCondition'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(r1.json()["data"]["total"]) == str(project_data['exp']['datatotal'])

def test_project(project_data, url, br, db_info):
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    account.changeCompanyLogin(url, br,  headers,project_data['changeCompanyLogin'])
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1=project.getActivityLogByCreateId(url,headers, br,project_data['getActivityLogByCreateId'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(r1.json()["data"]["totalNumber"]) >= str(project_data['exp']['getActivityLog'])

def test_project2(project_data, url, br, db_info):
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    account.changeCompanyLogin(url, br, headers, project_data['changeCompanyLogin'])
    r1=project.listProjectByCondition(url, br,headers, project_data['listProjectByCondition'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(r1.json()["code"]) == str(project_data['exp']['code'])
    assert str(r1.json()["data"]["total"]) != str(project_data['exp']['getActivityLog'])

# 归档项目
# 已有重复的
# def test
# updateProjectDataType_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     print(r.json())
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.updateProjectDataType(url,br,headers,project_data['updateProjectDataType'])
#     print(r1.json())
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# 将项目从回收站里删除
# 已有重复
# def test_delete_project2(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.deleteProject2(url,br,headers,project_data['deleteProject2'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])


# 从回收站恢复项目
# def test_recover_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.recoverProject(url,br,headers,project_data['recoverProject'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# 添加项目成员
# def test_changeResourc_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.changeProjectResourc(url,br,headers,project_data['changeProjectResourc'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# 获取relId
# 这一步是先增加
# def test_addUserRelId_project(project_data,url,br,getHeaders):
#     r = project.changeProjectResourc(url, br,getHeaders, project_data['changeProjectResourc'])
#     print(r.json())
#     assert str(r.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r.json()['message']) == str(project_data['exp']['message'])

# 这一步是获取relId
# def test_getUserRelId_project(project_data,url,br,getHeaders):
#     r = project.getUserIdsByProjectId(url,br,getHeaders,project_data['getUserIdsByProjectId'])
#     assert str(r.json()['message'])==str(project_data['exp']['message'])
#     assert str(r.json()['code'])==str(project_data['exp']['code'])
#     relId=jsonpath.jsonpath(r.json(),"$..relId")
#     return relId


# 移除项目成员
# 已有重复代码
# def test_deleteResourc_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.deleteProjectResource(url,br,headers,project_data['deleteProjectResource'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# 使用项目模板新建项目
# def test_copeByProjectId_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.copeProjectByProjectId(url,br,headers,project_data['copeProjectByProjectId'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# 删除项目模板
# def test_deletecopyProject_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.deletecopyProject(url, br, headers, project_data['deletecopyProject'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])

# 复制项目模板
# def test_copyProjectTemplate_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.copyProjectTemplate(url, br, headers, project_data['copyProjectTemplate'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])


# 添加项目
# def test_add_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.addProject(url, br, headers, project_data['addProject'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])
#     projectIds= {
#         "projectIds": [r1.json()["data"]]
#     }
#     r1= project.deleteProject(url, br, headers,projectIds )
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])

# 删除项目
# def test_delete_project(project_data, url, br):
#     r = member.login(url, br, project_data['logindata'])
#     print(r.json())
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.deleteProject(url,br,headers,project_data['deleteProject'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# 添加任务
# def test_addTask_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.addTask(url, br, headers, project_data['addTask'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])

# 激活已归档的项目
# def test_updateDataType1_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.updateProjectDataType1(url, br, headers, project_data['updateProjectDataType1'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])
#
# #将已归档的项目移至回收站
# def test_updateDataType2_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.updateProjectDataType2(url, br, headers, project_data['updateProjectDataType2'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])

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
def test_getUserIdsByProjectId_project(project_data,url,br):
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    account.changeCompanyLogin(url, br, headers,project_data['changeCompanyLogin'])
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1 = project.getUserIdsByProjectId(url, br, headers, project_data['getUserIdsByProjectId'])
    assert str(r1.json()["code"]) == str(project_data['exp']['code'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])

#查询登录用户所参与的企业
def test_queryCompanyListByUserId(project_data,url,br,getHeaders):

    queryCompanyListByUserId={
        "pageType": 1
    }
    r1= account.queryCompanyListByUserId(url,br,getHeaders,queryCompanyListByUserId)
    print(len(r1.json()["data"]))
    assert str(r1.json()["code"]) == str(project_data['exp']['code'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(len(r1.json()["data"])) < str(project_data['exp']['datatotal'])

