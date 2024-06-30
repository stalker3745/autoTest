'''
项目相关接口
'''

def batchOperationTask(url,br,headers,cs):  # 获取用户列表
    url = url + "/newTask/batchOperationTask"
    r = br.post_hearder(url,headers,json=cs)
    return r