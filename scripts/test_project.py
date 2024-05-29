import  pytest
# µÇÂ¼µÄÊý¾Ý
from baw import account
from baw import project
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/Project.yaml"))
def project_data(request):
    return request.param


def test_project(project_data, url, br, db_info):
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    account.changeCompanyLogin(url,headers, br, project_data['changeCompanyLogin'])
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
    account.changeCompanyLogin(url, headers, br, project_data['changeCompanyLogin'])
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1=project.getActivityLogByCreateId(url,headers, br,project_data['getActivityLogByCreateId'])
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(r1.json()["data"]["totalNumber"]) >= str(project_data['exp']['getActivityLog'])

def test_project(project_data, url, br, db_info):
    r = member.login(url, br, project_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    # account.changeCompanyLogin(url, headers, br, project_data['changeCompanyLogin'])
    r1=project.listProjectByCondition(url, br,headers, project_data['listProjectByCondition'])
    print(r1.json())
    assert str(r1.json()['message']) == str(project_data['exp']['message'])
    assert str(r1.json()["code"]) == str(project_data['exp']['code'])
    assert str(r1.json()["data"]["total"]) != str(project_data['exp']['getActivityLog'])
