from time import sleep
import pytest
from baw import member, project
from caw import fileRead

#前置登录的数据
# @pytest.fixture(scope='module',params=fileRead.read_yaml("/data_case/login.yaml"))
# #定义一个方法 通过request获取每一组数据（固定的格式）
# def login_data(request):
#     return request.param
#前置方法
# @pytest.fixture(scope='module')
# def prepare(login_data, url , br):
#     r = member.login(url, br, login_data['logindata'])
#     # 校验登录的结果
#     assert str(r.json()['message']) == str(login_data['exp']['message'])
#     assert str(r.json()['code']) == str(login_data['exp']['code'])
#     headers = {
#         'Authorization': r.json()["data"]["jwtToken"],
#         'User-Company': r.json()["data"]["companyId"]}
#     print(headers)
#     return headers

#获取创建任务的数据
@pytest.fixture(scope='module',params=fileRead.read_yaml("/data_case/addtask.yaml"))
def task_data(request):
    return request.param
#下方创建任务的请求
def test_addproject(getHeaders,url,br,task_data):
    print(f"新增任务成功的功能，测试数据为：{task_data}")
    sleep(1)
    r = project.add_task(url, br ,getHeaders,task_data['taskdata'])
    print(f"创建任务：{r}")
    # 校验添加用户的结果
    assert str(r.json()['message']) == str(task_data['exp']['message'])
    assert str(r.json()['code']) == str(task_data['exp']['code'])

