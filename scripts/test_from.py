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
    print(rx.json())
    rx = from1.getAppById(url, headers,br, form_data['getAppById'])
    print(rx.json())

    viewId=from1.getFormViewConfigList(url,headers, br, form_data['logindata'])
    getFromFieldEnumList = {'language': "CN",
                   'companyId': r.json()["data"]["companyId"],
                    "viewId":"1217619369606336512",
                    "viewIden": 1,
                    "fieldId": "fd_1676955337149member",
                    "appId": "1075773133891485696"
                            }
    r1=from1.getFromFieldEnumList(url,headers, br,getFromFieldEnumList)
    assert str(r1.json()['message']) == str(form_data['exp']['message'])
    print(r1.json())
