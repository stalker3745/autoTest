'''
项目相关接口
'''

# 查看项目日志
def getActivityLogByCreateId(url,headers, br,cs):
    url = url + "/newProject/getActivityLogByCreateId"
    r = br.post_hearder(url,headers,json=cs)
    return r


# 新增项目
def addProject(url,br,headers,cs):
    url=url+"/newProject/addProject"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 获取用户列表
def listProjectByCondition(url,br,headers,cs):
    url = url + "/newProject/listProjectByCondition"
    r = br.post_hearder(url,headers,json=cs)
    return r

# 删除项目+删除回收站里的项目
def deleteProject(url,br,headers,cs):
    url = url + "/newProject/deleteProject"
    r = br.post_hearder(url,headers,json=cs)
    return r

# 更新项目，回复项目,删除项目，项目归档
def updateProjectDataType(url,br,headers,cs):
    url= url+"/newProject/updateProjectDataType"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 创建项目模板和使用项目模板新建项目
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

# 打开项目设置应用中指定功能
def updateProjectAPPByProjectId(url,br,headers,cs):
    url=url+"/newProject/updateProjectAPPByProjectId"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 查看所有项目
def getProjectList(url,br,headers,cs):
    url = url + "/newProject/getProjectList"
    r = br.post_hearder(url, headers, json=cs)
    return r

# 获取实时relId(与下列移除项目成员同时使用)
def getUserRelId(url,br,headers,cs):
    url=url+"/projectResource/getUserIdsByProjectId"
    r = br.post_hearder(url, headers, json=cs)
    return r

# 添加项目成员
def changeProjectResourc(url,br,headers,cs):
    url=url+"/projectResource/changeProjectResource"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 移除项目成员
def deleteProjectResource(url,br,headers,cs):
    url=url+"/projectResource/deleteProjectResource"
    r=br.post_hearder(url,headers,json=cs)
    # r1=response.json()
    # relId=r1.get("result")[0].get("relId")
    return r

# 查看该项目下所有的成员
def getUserIdsByProjectId(url,br,headers,cs):
    url=url+"/projectResource/getUserIdsByProjectId"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 更改项目阶段和开启阶段更新自动化
def updateProjectPahseParams(url,br,headers,cs):
    url=url+"/projectPhase/updateProjectPahseParams"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 展示阶段列表
def getProjectPahseScheduleList(url,br,headers,cs):
    url=url+"/projectPhase/getProjectPahseScheduleList"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 添加项目管理阶段中的管理状态
def changeProjectPahse(url,br,headers,cs):
    url=url+"/projectPhase/changeProjectPahse"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 查看所有的任务和子任务
def listTreeTask(url,br,headers,cs):
    url=url+"/newTask/listTreeTask"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 添加任务站点
def addProjectSite(url,br,headers,cs):
    url=url+"/projectSite/addProjectSite"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 添加任务和任务底下的子任务
def addTask(url,br,headers,cs):
    url=url+"/newTask/addNewTask"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 查看项目下的部门
def listDept(url,br,headers,cs):
    url=url+"/deptManager/listDept"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 查看公司下的成员
def listCompanyUserPage(url,br,headers,cs):
    url=url+"/user/company/listCompanyUserPage"
    r=br.post_hearder(url,headers,json=cs)
    return r

# 获取项目id
def getProjectById(url,br,headers,cs):
    url=url+"/newProject/getProjectById"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 添加项目文件夹
def addCustomFolder(url,br,headers,cs):
    url=url+"/documentManager/addCustomFolder"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 通过项目Id获取相应参数
def getProjectById(url,br,headers,cs):
    url=url+"/newProject/getProjectById"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 查看项目文件夹列表
def listCustomDocument(url,br,headers,cs):
    url=url+"/documentManager/listCustomDocument"
    r=br.post_hearder(url, headers, json=cs)
    return r

# 删除项目文件夹
def operationDocument(url,br,headers,cs):
    url=url+"/documentManager/operationDocument"
    r=br.post_hearder(url,headers,json=cs)
    return r