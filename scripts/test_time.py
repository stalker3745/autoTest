# -*- coding: utf-8 -*-
import os
from datetime import datetime

import pytest
import requests
import pandas as pd

class TestTime:
    # 原始url
    url = 'https://user.zdsztech.com/employee-web-application'
    login_url='https://user.zdsztech.com/employee-web-application/account/mixLogin'
    headers = {"Content-Type": "application/json;charset=utf8"}
    username = "mazhenhua2@zdsztech.com"
    password = "dog7jCEMgBCy02XUcrsv4w=="
    login_data = {"account": "mazhenhua2@zdsztech.com", "password": "dog7jCEMgBCy02XUcrsv4w==", "language": "CN"}  # 配置用户登录的账号

    # 接口
    url1 = '/appPageDesign/getAppPageDesignByCondition'
    url2 = '/companyEquity/getCompanySolutionConfig'
    url3 = '/app/getAppPackageList'
    url4 = '/appPageDesign/getAppPageDesignByCondition'
    url5 = '/app/getAppListByPackage'
    url6 = '/view/getFromListViewData'
    url7 = '/form/getEnableFormVueMetaDataByAppId'
    url8 = '/form/getDraftDataCount'

    # @pytest.fixture(scope='session')
    def login(self,login_url,login_data):
        r = requests.post(login_url, json=login_data)
        print(r.json())
        return r

    # 获取getAppPageDesignByCondition的请求时间
    def test_getAppPageDesignByCondition_time(self):
        r = self.login(self.login_url,self.login_data)

        headers = {
            'Authorization': r.json()["data"]["jwtToken"],
             "User-Company": "1069317931558674432"
        }

        data = {
          "companyId": r.json()["data"]["companyId"],
          "appId": "1255086419890810926",
          "isEnable": "true",
          "isProjectEnter": "false"
        }
        # POST请求
        response = requests.post(self.url + self.url1, json=data,
                                     headers=headers)

        # 获取接口请求时间
        time = response.elapsed.total_seconds()*1000
        print(f"getAppPageDesignByCondition的接口请求时间：{time}毫秒")

        # 断言
        assert response.status_code == 200
        assert response.json()['message'] == "操作成功!"

    # 获取getCompanySolutionConfig的请求时间
    def test_getCompanySolutionConfig_time(self):
        r = self.login(self.login_url, self.login_data)

        headers = {
            "Authorization": r.json()["data"]["jwtToken"],
            "User-Company": "1069317931558674432"
        }

        data = {
             "companyId":  r.json()["data"]["companyId"],
             "businessSystemId": "1255086411552534528"
        }

        response = requests.post(self.url + self.url2, json=data,headers=headers)
        time = response.elapsed.total_seconds()*1000
        print(f"getCompanySolutionConfig的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200
        assert response.json()['message'] == "操作成功!"

    # 获取getAppPackageList的请求时间
    def test_getAppPackageList_time(self):
        r = self.login(self.login_url, self.login_data)

        headers = {
            "Authorization": r.json()["data"]["jwtToken"],
            "User-Company": "1069317931558674432",
            "Lang": "CN"
        }

        data = {
           "companyId":  r.json()["data"]["companyId"],
           "businessSystemId": "1255086411552534528",
           "isLook": "true"
        }
        response = requests.post(self.url + self.url3, json=data, headers=headers)
        time = response.elapsed.total_seconds()*1000
        print(f"getAppPackageList的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200
        assert response.json()['message'] == "操作成功!"

    # 获取getAppPageDesignByCondition的请求时间
    def test_getAppPageDesignByCondition_time(self):
        r = self.login(self.login_url, self.login_data)
        headers = {
            "Authorization": r.json()["data"]["jwtToken"],
            "User-Company": "1069317931558674432",
            "Lang": "CN"
        }

        data = {
           "companyId":  r.json()["data"]["companyId"],
           "appId": "1255086419890810926",
           "isEnable": "true",
           "isProjectEnter": "false"
        }
        response = requests.post(self.url + self.url4, json=data, headers=headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getAppPageDesignByCondition的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200
        assert response.json()['message'] == "操作成功!"

    # 获取getAppListByPackage的请求时间
    def test_getAppListByPackage_time(self):
        r = self.login(self.login_url, self.login_data)

        headers = {
            "Authorization": r.json()["data"]["jwtToken"],
            "User-Company": "1069317931558674432",
            "Lang": "CN"
        }

        data = {
            "companyId":  r.json()["data"]["companyId"],
            "searchName": "",
            "appGroupId": "1255086413528051714",
            "projectId": "",
            "isLook": "true"
        }
        response = requests.post(self.url + self.url5, json=data, headers=headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getAppListByPackage的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200
        assert response.json()['message'] == "操作成功!"

    # 获取getFromListViewData的请求时间
    def test_getFromListViewData_time(self):
        r = self.login(self.login_url, self.login_data)

        headers = {
            "Authorization": r.json()["data"]["jwtToken"],
            "User-Company": "1069317931558674432",
            "Lang": "CN"
        }

        data = {
            "page": 1,
            "pageSize": 20,
            "type": "pageDesigner",
            "appId": "1255086419890810892",
            "companyId": r.json()["data"]["companyId"],
            "pageAppId": "1255086419890810930",
            "viewId": "1255086489709195283",
            "viewListTotal": 10,
            "sortRuleList": [],
            "isDddPermissions": "true",
            "viewIden": 1,
            "conditionGroupList": [],
            "conditionLinkType": "and"
        }
        response = requests.post(self.url + self.url6, json=data, headers=headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getFromListViewData的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200
        assert response.json()['message'] == "操作成功!"

    # 获取getFromListViewData的请求时间
    def test_getEnableFormVueMetaDataByAppId_time(self):
        r = self.login(self.login_url, self.login_data)
        headers = {
            "Authorization": r.json()["data"]["jwtToken"],
            "User-Company": "1069317931558674432",
            "Lang": "CN"
        }

        data ={
            "companyId": r.json()["data"]["companyId"],
            "appId": "1255086419890810912"
        }
        response = requests.post(self.url + self.url7, json=data, headers=headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getEnableFormVueMetaDataByAppId的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200
        assert response.json()['message'] == "操作成功!"

    # 获取getFromListViewData的请求时间
    def test_getDraftDataCount_time(self):
        r = self.login(self.login_url, self.login_data)
        headers = {
            "Authorization": r.json()["data"]["jwtToken"],
            "User-Company": "1069317931558674432",
            "Lang": "CN"
        }

        data = {
            "appId": "1255086419890810912",
            "companyId": r.json()["data"]["companyId"]
        }
        response = requests.post(self.url + self.url8, json=data, headers=headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getDraftDataCount的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200
        assert response.json()['message'] == "操作成功!"

    # 将数据放入Excel表格
    def test_saveExcel_time(self):
        dataExcel = {
            "接口名称": ["getAppPageDesignByCondition", "getCompanySolutionConfig", "getAppPackageList",
                         "getAppPageDesignByCondition", "getAppListByPackage", "getFromListViewData",
                         "getEnableFormVueMetaDataByAppId", "getDraftDataCount"],
            "接口运行时长（毫秒）": []
        }
        print(dataExcel)

        # 获取每个接口的请求时间
        for url in [self.url1, self.url2, self.url3, self.url4, self.url5, self.url6, self.url7, self.url8]:
            response = requests.post(self.url + url, json=self.login_data, headers=self.headers)
            time_ms = response.elapsed.total_seconds() * 1000
            dataExcel["接口运行时长（毫秒）"].append(time_ms)

        print(dataExcel)
        # 将数据存储到Excel表格
        df = pd.DataFrame(dataExcel)
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        print(desktop_path)
        today = datetime.today()
        year = today.year
        month = today.month
        day = today.day

        file_path = os.path.join(desktop_path, f"{year}年接{month}月{day}接口运行时长统计.xlsx")
        df.to_excel(file_path, index=False)

        print(f"{year}年{month}月{day}日的接口运行时长已保存到{file_path}")
