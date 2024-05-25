import time

import pytest

# 登录的数据
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/SubmitFormData.yaml"))
def login_data(request):
    return request.param

# 登录的测试步骤
def test_SubmitFormData(login_data, url, br, db_info):
    # 下发登录的请求
    r = member.login(url, br, login_data['logindata'])
    # print(r.json()["data"]["companyId"])
    # print(r.json()["data"]["jwtToken"])
    # 校验登录的结果
    assert str(r.json()['message']) == str(login_data['exp']['message'])
    assert str(r.json()['code']) == str(login_data['exp']['code'])
    if r.json()['message']=="操作成功!":
        headers = {'Lang': "CN",
                   'Authorization': r.json()["data"]["jwtToken"],
                   'User-Company': r.json()["data"]["companyId"]}
        # print(member.notice(url, headers, br,login_data['note']))
        # print(member.newGetFormDetailData(url, headers, br,login_data['getlog']).json()["data"]["gmtModified"])
        r=member.newGetFormDetailData(url, headers, br,login_data['getlog'])
        gmtModified=r.json()["data"]["gmtModified"]
        formMetaDataDetailsVO=r.json()["data"]["formMetaDataDetailsVO"]
        appId=r.json()["data"]["appId"]
        # entityId=r.json()["data"]["entityId"]
        # "dataId": entityId,
        # "entityId": entityId,
        companyId=r.json()["data"]["companyId"]
        login_data1={"formMetaDataDetailsVO":formMetaDataDetailsVO,
        "gmtModified":gmtModified,
        "companyId": companyId,
        "appId": appId,
        "isPass": "true",
        "mode": 2,
        "isEdit": "true",
        "isAdminEdit": "true"}
        r1=member.newSubmitFormData(url, headers, br,login_data1)
        assert str(r1.json()['message']) == str(login_data['exp']['message'])
        assert str(r1.json()['code']) == str(login_data['exp']['code'])
        time.sleep(3)
        login_data1 = {"formMetaDataDetailsVO": formMetaDataDetailsVO,
                       "appId": appId,
                       "companyId": companyId,
                       "dataId":  r1.json()["data"]["entityId"],
                       "entityId": r1.json()["data"]["entityId"],
                       "gmtModified": "2023-02-04 14:44:08.000",
                       "isPass": "true",
                       "mode": 2,
                       "isEdit": "true",
                       "isAdminEdit": "true"}
        print(login_data1)
        r1=member.newSubmitFormData(url, headers, br,login_data1)
        print(r1.json())
