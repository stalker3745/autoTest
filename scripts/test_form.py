import  pytest
import time

# 登录的数据
from caw import db
from baw import form
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/form.yaml"))
def form_data(request):
    return request.param


def test_from_1(form_data, url, br,getHeaders):
    rx= form.getAppListByPackage(url,getHeaders, br, form_data['getAppListByPackage'])
    assert str(rx.json()['message']) == str(form_data['exp']['message'])
    assert str(rx.json()['code']) == str(form_data['exp']['code'])
    rx = form.getAppById(url, getHeaders,br, form_data['getAppById'])
    assert str(rx.json()['message']) == str(form_data['exp']['message'])
    assert str(rx.json()['code']) == str(form_data['exp']['code'])
    form1=form.getFormViewConfigList(url,getHeaders, br, form_data['getFormViewConfigList'])
    assert str(form1.json()['message']) == str(form_data['exp']['message'])
    assert str(form1.json()['code']) == str(form_data['exp']['code'])
    viewId=form1.json()["data"][0]["viewId"]
    viewIden=form1.json()["data"][0]["viewType"]
    getFromFieldEnumList = {'language': "CN",
                   'companyId': getHeaders["User-Company"],
                    "viewId":viewId,
                    "viewIden": viewIden,
                    "fieldId": "fd_1676955337149member",
                    "appId": form_data['getAppById']["appId"]
                            }
    r1=form.getFromFieldEnumList(url,getHeaders, br,getFromFieldEnumList)
    assert str(r1.json()['message']) == str(form_data['exp']['message'])
    assert str(r1.json()['code']) == str(form_data['exp']['code'])
    assert len(r1.json()["data"]) == form_data['exp']['int1']



#前置方法
# @pytest.fixture(scope='module')
# def prepare(form_data, url , br):
#     r = member.login(url, br,form_data['logindata'])
#     # 校验登录的结果
#     assert str(r.json()['message']) == str(form_data['exp']['message'])
#     assert str(r.json()['code']) == str(form_data['exp']['code'])
#     prepare = {'Lang': "CN",
#                 'Authorization': r.json()["data"]["jwtToken"],
#                 'User-Company': r.json()["data"]["companyId"]}
#     return prepare

# 登录的测试步骤
def test_SubmitFormData(form_data,getHeaders, url, br, db_info):
    # 删除多余数据
    db.updata_formentity(db_info, form_data['appidend'])
    r=member.newGetFormDetailData(url, getHeaders, br,form_data['getlog'])
    gmtModified=r.json()["data"]["gmtModified"]
    formMetaDataDetailsVO=r.json()["data"]["formMetaDataDetailsVO"]
    appId=r.json()["data"]["appId"]
    companyId=r.json()["data"]["companyId"]
    form_data1={"formMetaDataDetailsVO":formMetaDataDetailsVO,
    "gmtModified":gmtModified,
    "companyId": companyId,
    "appId": appId,
    "isPass": "true",
    "mode": 2,
    "isEdit": "true",
    "isAdminEdit": "true"}
    r1=member.newSubmitFormData(url, getHeaders, br,form_data1)
    assert str(r1.json()['message']) == str(form_data['exp']['message'])
    assert str(r1.json()['code']) == str(form_data['exp']['code'])
    time.sleep(3)
    form_data1 = {
        # "formMetaDataDetailsVO": formMetaDataDetailsVO,
                   "appId": appId,
                   "companyId": companyId,
                   "dataId":  r1.json()["data"]["entityId"],
                   "entityId": r1.json()["data"]["entityId"],
                   "isPass": "true",
                   "mode": 2,
                   "isEdit": "true",
                   "isAdminEdit": "true"}
    r=member.newGetFormDetailData(url, getHeaders, br,form_data1)
    form_data1 = {"formMetaDataDetailsVO": formMetaDataDetailsVO,
                            "appId": appId,
                            "companyId": companyId,
                            "dataId": r.json()["data"]["entityId"],
                            "entityId": r.json()["data"]["entityId"],
                            "gmtModified": r.json()["data"]["gmtModified"],
                            "isPass": "true",
                            "mode": 2,
                            "isEdit": "true",
                            "isAdminEdit": "true"}
    r1=member.newSubmitFormData(url, getHeaders, br,form_data1)
    assert str(r1.json()['code']) == str(form_data['exp']['code'])
    assert str(r1.json()['message']) == str(form_data['exp']['message'])
    time.sleep(2)
    assert str(db.get_zd_form_entitydata(db_info, form_data['appidend'])[0][0]) == str(form_data['int1'])
    SubmitFormData_data1={"appId": appId,
                            "companyId": companyId,
                            "viewId": "39531",
                            "mode": 2,
                            "isLook": "false",
                            "isAdminEdit": "true"}
    r1=form.getFromListViewData(url, getHeaders, br,SubmitFormData_data1)
    print(r1.json()['data']["total"])
    assert str(r1.json()['code']) == str(form_data['exp']['code'])
    assert str(r1.json()['message']) == str(form_data['exp']['message'])
