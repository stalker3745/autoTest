import time

import pytest

# 登录的数据
from baw import member
from baw import from1
from caw import fileRead
from caw import db

@pytest.fixture(scope='module', params=fileRead.read_yaml("/data_case/SubmitFormData.yaml"))
def SubmitFormData_data(request):
    return request.param
#前置方法
@pytest.fixture(scope='module')
def prepare(SubmitFormData_data, url , br):
    r = member.login(url, br,SubmitFormData_data['logindata'])
    # 校验登录的结果
    assert str(r.json()['message']) == str(SubmitFormData_data['exp']['message'])
    assert str(r.json()['code']) == str(SubmitFormData_data['exp']['code'])
    prepare = {'Lang': "CN",
                'Authorization': r.json()["data"]["jwtToken"],
                'User-Company': r.json()["data"]["companyId"]}
    return prepare

# 登录的测试步骤
def test_SubmitFormData(SubmitFormData_data,prepare, url, br, db_info):
    # 删除多余数据
    db.updata_formentity(db_info, SubmitFormData_data['appidend'])
    r=member.newGetFormDetailData(url, prepare, br,SubmitFormData_data['getlog'])
    gmtModified=r.json()["data"]["gmtModified"]
    formMetaDataDetailsVO=r.json()["data"]["formMetaDataDetailsVO"]
    appId=r.json()["data"]["appId"]
    # entityId=r.json()["data"]["entityId"]
    # "dataId": entityId,
    # "entityId": entityId,
    companyId=r.json()["data"]["companyId"]
    SubmitFormData_data1={"formMetaDataDetailsVO":formMetaDataDetailsVO,
    "gmtModified":gmtModified,
    "companyId": companyId,
    "appId": appId,
    "isPass": "true",
    "mode": 2,
    "isEdit": "true",
    "isAdminEdit": "true"}
    r1=member.newSubmitFormData(url, prepare, br,SubmitFormData_data1)
    assert str(r1.json()['message']) == str(SubmitFormData_data['exp']['message'])
    assert str(r1.json()['code']) == str(SubmitFormData_data['exp']['code'])
    time.sleep(3)
    SubmitFormData_data1 = {
        # "formMetaDataDetailsVO": formMetaDataDetailsVO,
                   "appId": appId,
                   "companyId": companyId,
                   "dataId":  r1.json()["data"]["entityId"],
                   "entityId": r1.json()["data"]["entityId"],
                   "isPass": "true",
                   "mode": 2,
                   "isEdit": "true",
                   "isAdminEdit": "true"}
    r=member.newGetFormDetailData(url, prepare, br,SubmitFormData_data1)
    SubmitFormData_data1 = {"formMetaDataDetailsVO": formMetaDataDetailsVO,
                            "appId": appId,
                            "companyId": companyId,
                            "dataId": r.json()["data"]["entityId"],
                            "entityId": r.json()["data"]["entityId"],
                            "gmtModified": r.json()["data"]["gmtModified"],
                            "isPass": "true",
                            "mode": 2,
                            "isEdit": "true",
                            "isAdminEdit": "true"}
    r1=member.newSubmitFormData(url, prepare, br,SubmitFormData_data1)
    assert str(r1.json()['code']) == str(SubmitFormData_data['exp']['code'])
    assert str(r1.json()['message']) == str(SubmitFormData_data['exp']['message'])
    time.sleep(1)
    assert str(db.get_zd_form_entitydata(db_info, SubmitFormData_data['appidend'])[0][0]) == str(SubmitFormData_data['int1'])
    SubmitFormData_data1={"appId": appId,
                            "companyId": companyId,
                            "viewId": "39531",
                            "mode": 2,
                            "isLook": "false",
                            "isAdminEdit": "true"}
    r1=from1.getFromListViewData(url, prepare, br,SubmitFormData_data1)
    print(r1.json()['data']["total"])
    assert str(r1.json()['code']) == str(SubmitFormData_data['exp']['code'])
    assert str(r1.json()['message']) == str(SubmitFormData_data['exp']['message'])
