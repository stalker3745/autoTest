
def listAppDocument(url,headers, br,cs):  # ��ȡ�û��б�
    url = url + "/documentManager/listAppDocument"
    r = br.post_hearder(url,headers,json=cs)
    return r

def listShareDocument(url,headers, br,cs):  # ��ȡ�û��б�
    url = url + "/documentManager/listShareDocument"
    r = br.post_hearder(url,headers,json=cs)
    return r
