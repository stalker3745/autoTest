'''
用户管理模块的接口
'''
def register(url, br, cs):
    '''
    发送注册请求
    :param url:  测试环境地址，从env.ini文件中获取来的，url = http://user-sit.zdsztech.com
    :param br:  BaseRequests的实例
    :param cs:  参数
    :return:
    '''
    url = url + "/futureloan/mvc/api/member/register"
    r = br.post(url, data=cs)
    return r

def login(url, br, cs):  # 登录
    url = url + "/employee-web-application/account/mixLogin"
    r = br.post(url, json=cs)
    return r

def list(url, br):  # 获取用户列表
    url = url + "/futureloan/mvc/api/member/list"
    r = br.get(url)
    return r

def notice(url,headers, br,cs):  # 获取用户列表
    url = url + "/employee-web-application/noticeController/NoticeList"
    r = br.post_log(url,headers,json=cs)
    return r
def newSubmitFormData(url,headers, br,cs):  # 获取用户列表
    url = url + "/employee-web-application/app/newSubmitFormData"
    r = br.post_log(url,headers,json=cs)
    return r
def newGetFormDetailData(url,headers, br,cs):  # 获取用户列表
    url = url + "/employee-web-application/app/newGetFormDetailData"
    r = br.post_log(url,headers,json=cs)
    return r
