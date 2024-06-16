import  pytest

# ��¼������
from baw import account,project,member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/Project.yaml"))
def project_data(request):
    return request.param

#��ѯ����Ŀ��
def test_allProject_project(project_data, url, br, getHeaders):
    account.changeCompanyLogin(url, br, getHeaders, project_data['changeCompanyLogin'])
    listAllProjectByCondition= {"dataType":"1" }
    r1=project.listAllProjectByCondition(url,getHeaders, br,listAllProjectByCondition)
    print(r1.json()["data"]["total"])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(r1.json()["data"]["total"]) >= str(project_data['exp']['datatotal'])
#��ѯ������Ŀ��
def test_project(project_data, url, br, getHeaders):
    account.changeCompanyLogin(url, br,  getHeaders,project_data['changeCompanyLogin'])
    r1=project.getActivityLogByCreateId(url,getHeaders, br,project_data['getActivityLogByCreateId'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(r1.json()["data"]["totalNumber"]) >= str(project_data['exp']['getActivityLog'])

#��ѯ��������
def test_project2(project_data, url, br, getHeaders):
    listProjectByCondition=  {"projectName":"pytest","dataType": 1 }
    account.changeCompanyLogin(url, br, getHeaders, project_data['changeCompanyLogin'])
    r1=project.listProjectByCondition(url, br,getHeaders, listProjectByCondition)
    print(r1.json()["data"])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(r1.json()["code"]) == str(project_data['exp']['code'])
    assert str(r1.json()["data"]["total"]) != str(project_data['exp']['getActivityLog'])

#��ѯ��¼�û����������ҵ
def test_queryCompanyListByUserId(project_data,url,br,getHeaders):
    queryCompanyListByUserId={
        "pageType": 1
    }
    r1= account.queryCompanyListByUserId(url,br,getHeaders,queryCompanyListByUserId)
    print(len(r1.json()["data"]))
    assert str(r1.json()["code"]) == str(project_data['exp']['code'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(len(r1.json()["data"])) > str(project_data['exp']['datatotal'])

# �鵵��Ŀ
# �����ظ���
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

# ����Ŀ�ӻ���վ��ɾ��
# �����ظ�
# def test_delete_project2(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.deleteProject2(url,br,headers,project_data['deleteProject2'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])


# �ӻ���վ�ָ���Ŀ
# def test_recover_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.recoverProject(url,br,headers,project_data['recoverProject'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# �����Ŀ��Ա
# def test_changeResourc_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.changeProjectResourc(url,br,headers,project_data['changeProjectResourc'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# ��ȡrelId
# ��һ����������
# def test_addUserRelId_project(project_data,url,br,getHeaders):
#     r = project.changeProjectResourc(url, br,getHeaders, project_data['changeProjectResourc'])
#     print(r.json())
#     assert str(r.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r.json()['message']) == str(project_data['exp']['message'])

# ��һ���ǻ�ȡrelId
# def test_getUserRelId_project(project_data,url,br,getHeaders):
#     r = project.getUserIdsByProjectId(url,br,getHeaders,project_data['getUserIdsByProjectId'])
#     assert str(r.json()['message'])==str(project_data['exp']['message'])
#     assert str(r.json()['code'])==str(project_data['exp']['code'])
#     relId=jsonpath.jsonpath(r.json(),"$..relId")
#     return relId


# �Ƴ���Ŀ��Ա
# �����ظ�����
# def test_deleteResourc_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.deleteProjectResource(url,br,headers,project_data['deleteProjectResource'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# ʹ����Ŀģ���½���Ŀ
# def test_copeByProjectId_project(project_data,url,br):
#     r=member.login(url,br,project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.copeProjectByProjectId(url,br,headers,project_data['copeProjectByProjectId'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# ɾ����Ŀģ��
# def test_deletecopyProject_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.deletecopyProject(url, br, headers, project_data['deletecopyProject'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])

# ������Ŀģ��
# def test_copyProjectTemplate_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.copyProjectTemplate(url, br, headers, project_data['copyProjectTemplate'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])


# �����Ŀ
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

# ɾ����Ŀ
# def test_delete_project(project_data, url, br):
#     r = member.login(url, br, project_data['logindata'])
#     print(r.json())
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1=project.deleteProject(url,br,headers,project_data['deleteProject'])
#     assert str(r1.json()["code"])==str(project_data['exp']['code'])
#     assert str(r1.json()['message'])==str(project_data['exp']['message'])

# �������
# def test_addTask_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.addTask(url, br, headers, project_data['addTask'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])

# �����ѹ鵵����Ŀ
# def test_updateDataType1_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.updateProjectDataType1(url, br, headers, project_data['updateProjectDataType1'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])
#
# #���ѹ鵵����Ŀ��������վ
# def test_updateDataType2_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.updateProjectDataType(url, br, headers, project_data['updateProjectDataType2'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])

# �����Ŀ����׶��еĹ���״̬
# def test_changeProjectPahse_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.changeProjectPahse(url, br, headers, project_data['changeProjectPahse'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])

# �鿴��ǰ��Ŀ�����еĳ�Ա
# def test_getUserIdsByProjectId_project(project_data,url,br):
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     account.changeCompanyLogin(url, br, headers,project_data['changeCompanyLogin'])
#     r = member.login(url, br, project_data['logindata'])
#     headers = {'Lang': "CN",
#                'Authorization': r.json()["data"]["jwtToken"],
#                'User-Company': r.json()["data"]["companyId"]}
#     r1 = project.getUserIdsByProjectId(url, br, headers, project_data['getUserIdsByProjectId'])
#     assert str(r1.json()["code"]) == str(project_data['exp']['code'])
#     assert str(r1.json()['message']) == str(project_data['exp']['message'])
