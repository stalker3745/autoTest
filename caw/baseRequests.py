'''
requests中的get、post包装一层，baseRequests
    使用session发送请求，用来保持用户的状态
    打印一些日志，方便定位问题
    异常处理
'''
import requests
class BaseRequests:
    def __init__(self):
        self.session = requests.session()  # 创建一个session

    def get(self, url, **kwargs):
        try:
            r = self.session.get(url, **kwargs)
            print(f"发送get请求成功，{url}，{kwargs}，响应信息为：{r.text}")
            return r
        except Exception as e:
            print(f"发送get请求异常，{url}，{kwargs}，异常信息为：{e}")

    def post(self, url, data=None, json=None, **kwargs):
        try:
            r = self.session.post(url, data=data, json=json, **kwargs)
            print(f"发送post请求成功，{url}，{data},{json},{kwargs}，响应信息为：{r.text}")
            return r
        except Exception as e:
            print(f"发送post请求异常，{url}，{data},{json},{kwargs}，异常信息为：{e}")

    def post_hearder(self, url, headers, data=None, json=None, **kwargs):
        try:
            r = self.session.post(url, headers=headers, data=data, json=json, **kwargs)
            # print(f"发送post请求成功，{url}，，{headers},{data},{json},{kwargs}，响应信息为：{r.text}")
            print(f"响应信息为：{r.text}")
            return r
        except Exception as e:
            print(f"发送post请求异常，{url}，{data},{json},{kwargs}，异常信息为：{e}")

import sys


# 测试代码，用完可以删除
if __name__ == '__main__':
    br = BaseRequests()
    # cs = {"mobilephone": "18012345678", "pwd": "123456"}
    # br.get("http://101.43.141.241:8088/futureloan/mvc/api/member/login", params=cs)
    br.post("http://user-sit.zdsztech.com/employee-web-application/account/mixLogin",
            json={"account":"15529310001","password":"dog7jCEMgBCy02XUcrsv4w==","language":"CN"})
print(sys.path)