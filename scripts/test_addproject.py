
import pytest
from baw import member, project, task
from caw import fileRead

#前置登录的数据
# @pytest.fixture(scope='module',params=fileRead.read_yaml("/data_case/login.yaml"))
# #定义一个方法 通过request获取每一组数据（固定的格式）
# def login_data(request):
#     return request.param
#前置方法 本文件只执行一次
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

#获取创建项目的数据
@pytest.fixture(params=fileRead.read_yaml("/data_case/addproject.yaml"))
def project_data(request):
    return request.param

#上面读取的数据通过参数传递都下面函数中使用
def test_addproject(url,br,getHeaders,project_data):
    # 下发创建项目的请求
    r = project.addProject(url, br ,getHeaders,project_data['addprojectdata'],)
    print(f"项目r：{r}")
    # 校验添加用户的结果
    assert str(r.json()['message']) == str(project_data['exp']['message'])
    assert str(r.json()['code']) == str(project_data['exp']['code'])
    projectIds={
        "projectIds": [r.json()["data"]]
    }
    r=project.deleteProject(url, br, getHeaders,projectIds)
    assert str(r.json()['message']) == str(project_data['exp']['message'])
    assert str(r.json()['code']) == str(project_data['exp']['code'])

# def test_deleteproject(url,br,getHeaders,project_data):
#     deg ={ "projectIds":
#           ['1257060083955974144',
# '1257060468141637632',"1257060879598665728"]
#     }
#     project.deleteProject(url,br,getHeaders,deg)

# def test_delettask(url,br,getHeaders,project_data):
#     dele={ "taskIdList":
#         ['1257060035041988608',
#         '1257060043434790912',
#         '1257060051831787520',
#         '1257060060220395520',
#         '1257060192601018368'],
#            "operationType": 5
#     }
#     task.batchOperationTask(url,br,getHeaders,dele)




