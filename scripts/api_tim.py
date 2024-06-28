# -*- coding: utf-8 -*-
import os
import time
from datetime import datetime
import requests
import schedule


class TestTime:
    # 原始url
    url = 'https://user.zdsztech.com/employee-web-application'
    # 接口
    url0= "https://user.zdsztech.com/employee-web-application/account/mixLogin"
    url1 = '/app/newGetFormDetailData'

    headers = {"Content-Type": "application/json;charset=utf8"}
    data = {"account": "mazhenhua16@zdsztech.com", "password": "dog7jCEMgBCy02XUcrsv4w==", "language": "CN"}  # 配置用户登录的账号
    data1 = {"appId":"1255935706610675763","companyId":"1069317931558674432","entityId":"1255935718811906055","withRealTimeData":"true","designTemplateId":"1255935933581242412","isProcessPermission":"false"}


    # 获取getAppPageDesignByCondition的请求时间
    def getAppPageDesignByCondition_time(self):
        # 发送POST请求
        r=requests.post(self.url0, json=self.data)
        headers={
            "Authorization": r.json()["data"]["jwtToken"],
            "Lang": "CN",
            'User-Company': r.json()["data"]["companyId"],
        }
        response = requests.post(self.url + self.url1, json=self.data1, headers=headers)
        # 获取接口请求时间
        time = response.elapsed.total_seconds()*1000
        # 断言请求是否成功
        assert response.status_code == 200
        return time


    # 填写公司表单样例代码
    def receiveData(self):
        time=datetime.now()
        time=time.strftime("%Y-%m-%d %H:%M")
        # 认证接口
        url1="http://api-sit.zdsztech.com/employee-web-application/systemCert/getTokenInfo"
        # 根据公司三方不同获取不同
        data= {"accessId":"V13qGN8a48","accessSecretKey":"ffac448f4ba6049f0c6830c5c897552c"}  # 登录的用户
        response = requests.post(url1, json=data)
        headers={
            "Authorization":response.json()["data"]["accessToken"]
        }
        data={
            "api": self.url1,
            "time": self.getAppPageDesignByCondition_time(),
            "time1": time
        }
        url="http://api-sit.zdsztech.com/employee-web-application/external/receiveData/5Jp0835545"
        response = requests.post(url, json=data, headers=headers)
        print(response.json())


if __name__== "__main__":
    # schedule.every(2).seconds.do()
    instance = TestTime()
    schedule.every().hours.do(instance.receiveData)
    # 无限循环以保持主线程运行
    while True:
        schedule.run_pending()
        time.sleep(100)


