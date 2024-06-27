# -*- coding: utf-8 -*-
import os
from datetime import datetime

import requests
import pandas as pd

from caw.baseRequests import BaseRequests as br


class TestTime:
    # 原始url
    url = 'https://user.zdsztech.com/employee-web-application'
    login_url='https://user.zdsztech.com/login'
    headers = {"Content-Type": "application/json;charset=utf8"}
    data = {"account": "mazhenhua2@zdsztech.com", "password": "dog7jCEMgBCy02XUcrsv4w==", "language": "CN"}  # 配置用户登录的账号

    def login(self,login_url,data):
        r = br.post(self,login_url, json=data)
        return r

    # 接口
    url1='/appPageDesign/getAppPageDesignByCondition'
    url2='/companyEquity/getCompanySolutionConfig'
    url3='/app/getAppPackageList'
    url4='/appPageDesign/getAppPageDesignByCondition'
    url5='/app/getAppListByPackage'
    url6='/view/getFromListViewData'
    url7='/form/getEnableFormVueMetaDataByAppId'
    url8='/form/getDraftDataCount'


    # 获取getAppPageDesignByCondition的请求时间
    def test_getAppPageDesignByCondition_time(self):
        self.login(self.login_url,self.data)
        # 发送POST请求
        response = requests.post(self.url + self.url1, json=self.data,
                                     headers=self.headers)

        # 获取接口请求时间
        time = response.elapsed.total_seconds()*1000
        print(f"getAppPageDesignByCondition的接口请求时间：{time}毫秒")

        # 断言请求是否成功
        assert response.status_code == 200

    # 获取getCompanySolutionConfig的请求时间
    def test_getCompanySolutionConfig_time(self):
        self.login(self.login_url, self.data)
        response = requests.post(self.url + self.url2, json=self.data,headers=self.headers)
        time = response.elapsed.total_seconds()*1000
        print(f"getCompanySolutionConfig的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200

    # 获取getAppPackageList的请求时间
    def test_getAppPackageList_time(self):
        self.login(self.login_url, self.data)
        response = requests.post(self.url + self.url3, json=self.data, headers=self.headers)
        time = response.elapsed.total_seconds()*1000
        print(f"getAppPackageList的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200

    # 获取getAppPageDesignByCondition的请求时间
    def test_getAppPageDesignByCondition_time(self):
        self.login(self.login_url, self.data)
        response = requests.post(self.url + self.url4, json=self.data, headers=self.headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getAppPageDesignByCondition的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200

    # 获取getAppListByPackage的请求时间
    def test_getAppListByPackage_time(self):
        self.login(self.login_url, self.data)
        response = requests.post(self.url + self.url5, json=self.data, headers=self.headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getAppListByPackage的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200

    # 获取getFromListViewData的请求时间
    def test_getFromListViewData_time(self):
        self.login(self.login_url, self.data)
        response = requests.post(self.url + self.url6, json=self.data, headers=self.headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getFromListViewData的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200

    # 获取getFromListViewData的请求时间
    def test_getEnableFormVueMetaDataByAppId_time(self):
        self.login(self.login_url, self.data)
        response = requests.post(self.url + self.url7, json=self.data, headers=self.headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getEnableFormVueMetaDataByAppId的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200

    # 获取getFromListViewData的请求时间
    def test_getDraftDataCount_time(self):
        self.login(self.login_url, self.data)
        response = requests.post(self.url + self.url8, json=self.data, headers=self.headers)
        time = response.elapsed.total_seconds() * 1000
        print(f"getDraftDataCount的接口请求时间：{time}毫秒")
        # 断言请求是否成功
        assert response.status_code == 200

    # 将数据放入Excel表格
    def test_saveExcel_time(self):
        data = {
            "接口名称": ["getAppPageDesignByCondition", "getCompanySolutionConfig", "getAppPackageList",
                         "getAppPageDesignByCondition", "getAppListByPackage", "getFromListViewData",
                         "getEnableFormVueMetaDataByAppId", "getDraftDataCount"],
            "接口运行时长（毫秒）": []
        }
        print(data)

        # 获取每个接口的请求时间
        for url in [self.url1, self.url2, self.url3, self.url4, self.url5, self.url6, self.url7, self.url8]:
            response = requests.post(self.url + url, json=self.data, headers=self.headers)
            time_ms = response.elapsed.total_seconds() * 1000
            data["接口运行时长（毫秒）"].append(time_ms)

        print(data)
        # 将数据存储到Excel表格
        df = pd.DataFrame(data)
        desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        print(desktop_path)
        today = datetime.today()
        year = today.year
        month = today.month
        day = today.day

        file_path = os.path.join(desktop_path, f"{year}年接{month}月{day}接口运行时长统计.xlsx")
        df.to_excel(file_path, index=False)

        print(f"{year}年{month}月{day}日的接口运行时长已保存到{file_path}")
