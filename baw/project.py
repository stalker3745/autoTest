'''
项目相关接口
'''
def listAllProjectByCondition(url,headers, br,cs):  # 获取用户列表
    url = url + "/newProject/listProjectByCondition"
    r = br.post_hearder(url,headers,json=cs)
    return r

def getActivityLogByCreateId(url,headers, br,cs):  # 获取用户列表
    url = url + "/newProject/getActivityLogByCreateId"
    r = br.post_hearder(url,headers,json=cs)
    return r


def add_project(url,br,headers,cs):
    url = url + "/newProject/addProject"
    r = br.post_hearder(url, headers,json=cs)
    return r

def add_task(url,br,headers,cs):
    url = url + "/newTask/addNewTask"
    r = br.post_hearder(url, headers,json=cs)
    return r
def listProjectByCondition(url,br,headers,cs):
    url = url + "/newProject/listProjectByCondition"
    r = br.post_hearder(url,headers,json=cs)
    return r
