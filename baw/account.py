'''
用户管理模块的接口
'''
def changeCompanyLogin(url,headers, br,cs):  # 获取用户列表
    url = url + "/account/changeCompanyLogin"
    r = br.post_hearder(url,headers,json=cs)
    return r

def queryCompanyListByUserId(url,br,headers,cs):
    url=url+"/user/company/queryCompanyListByUserId"
    r=br.post_hearder(url,headers,json=cs)
    return r