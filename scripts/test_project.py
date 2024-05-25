import  pytest

# µÇÂ¼µÄÊý¾Ý
from baw import project
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/Project.yaml"))
def login_data(request):
    return request.param


def test_project(login_data, url, br, db_info):
    r = member.login(url, br, login_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1=project.listAllProjectByCondition(url,headers, br,login_data['listAllProjectByCondition'])
    assert str(r1.json()['message']) == str(login_data['exp']['message'])
    assert str(r1.json()["data"]["total"]) == str(login_data['exp']['datatotal'])