import  pytest

# µÇÂ¼µÄÊý¾Ý
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/notice.yaml"))
def login_data(request):
    return request.param


def test_notice(login_data, url, br,db_info):
    r = member.login(url, br, login_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1=member.notice(url,headers, br,login_data['pares'])
    assert str(r1.json()['message']) == str(login_data['exp']['message'])
    r2=member.newGetMessageList(url,headers, br,login_data['newGetMessageList'])
    assert str(r2.json()['message']) == str(login_data['exp']['message'])
    assert str(r2.json()['data']["total"]) == str(login_data['expdate']['total'])

def test_newGetMessageList(login_data, url, br,db_info):
    r = member.login(url, br, login_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1=member.notice(url,headers, br,login_data['pares'])
    assert str(r1.json()['message']) == str(login_data['exp']['message'])
    r2=member.newGetMessageList(url,headers, br,login_data['newGetMessageList'])
    assert str(r2.json()['message']) == str(login_data['exp']['message'])
    assert str(r2.json()['data']["total"]) == str(login_data['expdate']['total'])