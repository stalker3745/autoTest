import  pytest

# µÇÂ¼µÄÊý¾Ý
from baw import from1
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/from.yaml"))
def form_data(request):
    return request.param


def test_from_1(form_data, url, br,db_info):
    r = member.login(url, br, form_data['logindata'])
    headers = {'Lang': "CN",
               'Authorization': r.json()["data"]["jwtToken"],
               'User-Company': r.json()["data"]["companyId"]}
    rx= from1.getAppListByPackage(url,headers, br, form_data['getAppListByPackage'])
    assert str(rx.json()['message']) == str(form_data['exp']['message'])
    assert str(rx.json()['code']) == str(form_data['exp']['code'])
    rx = from1.getAppById(url, headers,br, form_data['getAppById'])
    assert str(rx.json()['message']) == str(form_data['exp']['message'])
    assert str(rx.json()['code']) == str(form_data['exp']['code'])
    form1=from1.getFormViewConfigList(url,headers, br, form_data['getFormViewConfigList'])
    assert str(form1.json()['message']) == str(form_data['exp']['message'])
    assert str(form1.json()['code']) == str(form_data['exp']['code'])
    viewId=form1.json()["data"][0]["viewId"]
    viewIden=form1.json()["data"][0]["viewType"]
    getFromFieldEnumList = {'language': "CN",
                   'companyId': r.json()["data"]["companyId"],
                    "viewId":viewId,
                    "viewIden": viewIden,
                    "fieldId": "fd_1676955337149member",
                    "appId": form_data['getAppById']["appId"]
                            }
    r1=from1.getFromFieldEnumList(url,headers, br,getFromFieldEnumList)
    assert str(r1.json()['message']) == str(form_data['exp']['message'])
    assert str(r1.json()['code']) == str(form_data['exp']['code'])
    assert len(r1.json()["data"]) == form_data['exp']['int1']
