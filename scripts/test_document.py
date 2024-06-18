import  pytest

# µÇÂ¼µÄÊý¾Ý
from baw import document
from baw import member
from caw import fileRead

@pytest.fixture(params=fileRead.read_yaml("/data_case/all.yaml"))
def doc_data(request):
    return request.param


def test_doc_1(doc_data, url, br, getHeaders):
    # r = member.login(url, br, doc_data['logindata'])
    # headers = {'Lang': "CN",
    #            'Authorization': r.json()["data"]["jwtToken"],
    #            'User-Company': r.json()["data"]["companyId"]}
    listAppDocument= {"page": 1, "pageSize": 10, "companyId": getHeaders["User-Company"], "buildType": "1",
                      "parentRelId": "-1"}
    r1=document.listAppDocument(url,getHeaders, br,listAppDocument)
    assert str(r1.json()['message']) == str(doc_data['exp']['message'])
    assert str(r1.json()['code']) == str(doc_data['exp']['code'])
    print(r1.json()['data'][0]["attachmentName"])
    assert str(r1.json()['data'][0]["attachmentName"]) == str(doc_data['attachmentName']['attachmentName1'])

def test_doc_2(doc_data, url, br, getHeaders):
    # r = member.login(url, br, doc_data['logindata'])
    # headers = {'Lang': "CN",
    #            'Authorization': r.json()["data"]["jwtToken"],
    #            'User-Company': r.json()["data"]["companyId"]}
    listShareDocument= {"page": 1, "pageSize": 10, "companyId": getHeaders["User-Company"], "buildType": "1",
                        "parentRelId": "-1"}
    r1=document.listShareDocument(url,getHeaders, br,listShareDocument)
    assert str(r1.json()['message']) == str(doc_data['exp']['message'])
    assert str(r1.json()['code']) == str(doc_data['exp']['code'])
    assert str(r1.json()['data'][0]["attachmentName"]) == str(doc_data['attachmentName']['attachmentName2'])

