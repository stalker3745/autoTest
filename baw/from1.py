'''
用户管理模块的接口
'''
def getFromFieldEnumList(url,headers, br,cs):  # 获取用户列表
    url = url + "/form/getFromFieldEnumList"
    r = br.post_hearder(url,headers,json=cs)
    return r

def getFormViewConfigList(url,headers, br,cs):  # 获取用户列表
    url = url + "/view/getFormViewConfigList"
    r = br.post_hearder(url,headers,json=cs)
    return r

def getAppListByPackage(url,headers, br,cs):  # 获取用户列表
    url = url + "/app/getAppListByPackage"
    r = br.post_hearder(url,headers,json=cs)
    return r

def getAppById(url,headers, br,cs):  # 获取用户列表
    url = url + "/app/getAppById"
    r = br.post_hearder(url,headers,json=cs)
    return r