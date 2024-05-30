'''
项目相关接口
'''
import requests
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

# 添加项目成员
def changeProjectResourc(url,br,headers,cs):
    url=url+"/projectResource/changeProjectResource"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 获取实时relId(与下列移除项目成员同时使用)
# def getUserRelId(url,br,headers,cs):
#     url=url+"/projectResource/getUserIdsByProjectId"
#     r=requests.post_hearder(url,headers,json=cs)
#     data=br.json()
#     relId=data["relId"]
#     return relId,r


# 移除项目成员
def deleteProjectResource(url,br,headers,cs):
    url=url+"/projectResource/deleteProjectResource"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 使用项目模板新建项目
def copeProjectByProjectId(url,br,headers,cs):
    url=url+"/newProject/copeProjectByProjectId"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 删除项目模板
def deletecopyProject(url,br,headers,cs):
    url=url+"/newProject/deleteProject"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 复制项目模板
def copyProjectTemplate(url,br,headers,cs):
    url=url+"/newProject/copyProjectTemplate"
    r=br.post_hearder(url,headers,json=cs)
    return r