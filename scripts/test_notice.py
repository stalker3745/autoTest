# coding:utf-8
import  pytest

# 登录的数据
from baw import member
from caw import fileRead

# @pytest.fixture(params=fileRead.read_yaml("/data_case/notice.yaml"))
# def notice_data(request):
#     return request.param


def test_notice(url, br,getHeaders):
    pares= {"page": 1, "pageSize": 3}
    r1=member.notice(url,getHeaders, br,pares)
    assert str(r1.json()['message']) == "操作成功!"
    assert str(r1.json()['code']) == "200"

def test_newGetMessageList(url, br,getHeaders):
    newGetMessageList = {"page": 1, "pageSize": 10, "companyId": getHeaders["User-Company"], "messageGroupId": "5"}
    r2=member.newGetMessageList(url, getHeaders, br, newGetMessageList)
    assert str(r2.json()['message']) == "操作成功!"
    assert str(r2.json()['code']) == "200"
    assert str(r2.json()['data']["total"]) == "10"