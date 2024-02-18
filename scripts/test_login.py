import pytest

# 登录的数据
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/login.yaml"))
def login_data(request):
    return request.param

# 登录的测试步骤
def test_login(login_data, url, br, db_info):
    # 下发登录的请求
    r = member.login(url, br, login_data['logindata'])
    # 校验登录的结果
    assert str(r.json()['message']) == str(login_data['exp']['message'])
    assert str(r.json()['code']) == str(login_data['exp']['code'])

