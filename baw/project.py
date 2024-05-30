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

# 删除项目
def deleteProject(url,br,headers,cs):
    url = url + "/newProject/deleteProject"
    r = br.post_hearder(url,headers,json=cs)
    return  r

# 项目归档
def updateProjectDataType(url,br,headers,cs):
    url = url + "/newProject/updateProjectDataType"
    r = br.post_hearder(url,headers,json=cs)
    return r

# 删除回收站内的项目
def deleteProject2(url,br,headers,cs):
    url= url+"/newProject/deleteProject"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 回收站里恢复项目
def recoverProject(url,br,headers,cs):
    url= url+"/newProject/updateProjectDataType"
    r=br.post_hearder(url,headers,json=cs)
    return r