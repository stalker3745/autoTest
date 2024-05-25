import  pytest

# µÇÂ¼µÄÊý¾Ý
from baw import document
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/document.yaml"))
def login_data(request):
    return request.param


def test_doc_1(login_data, url, br, db_info):
    r = member.login(url, br, login_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1=document.listAppDocument(url,headers, br,login_data['listAppDocument'])
    assert str(r1.json()['message']) == str(login_data['exp']['message'])
    assert str(r1.json()['data'][0]["attachmentName"]) == str(login_data['attachmentName']['attachmentName1'])

def test_doc_2(login_data, url, br, db_info):
    r = member.login(url, br, login_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    r1=document.listShareDocument(url,headers, br,login_data['listShareDocument'])
    assert str(r1.json()['message']) == str(login_data['exp']['message'])
    assert str(r1.json()['data'][0]["attachmentName"]) == str(login_data['attachmentName']['attachmentName2'])

