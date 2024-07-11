# -*- coding: utf-8 -*-
import requests
import os
import time
import smtplib
import pytest
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
class TestLogin:
    # 登录配置信息
    url = 'https://user.zdsztech.com/employee-web-application'
    login_url = 'https://user.zdsztech.com/employee-web-application/account/mixLogin'
    headers = {"Content-Type": "application/json;charset=utf8"}
    username = "mazhenhua2@zdsztech.com"
    password = "dog7jCEMgBCy02XUcrsv4w=="
    login_data = {"account": "mazhenhua2@zdsztech.com", "password": "dog7jCEMgBCy02XUcrsv4w==", "language": "CN"}

    # 发送邮件配置信息
    path = os.path.join(os.getcwd(), "")
    case_path1 = os.path.join(path, "")
    report_path = os.path.join(os.path.join(os.getcwd()), "report")
    smtp_server = 'smtp.qq.com'
    smtp_port = 465
    sender_email = "27458625@qq.com"
    sender_password = "hfsnynuqbyghbjjc"
    subject = "测试报告"
    to_email = "2155745044@qq.com"

    # 发送邮件
    def send_email(self):
        body = "邮件正文内容发送 " + time.asctime()
        # 创建一个MIMEText邮件对象，HTML邮件正文
        message = MIMEMultipart()
        message.attach(MIMEText(body, "plain"))
        message['From'] = Header(self.sender_email)  # 邮件头部的From字段
        message['To'] = Header(self.to_email)  # 邮件头部的To字段
        message['Subject'] = Header(self.subject, 'utf-8')  # 邮件头部的主题

        attachment_path = os.path.join(self.report_path, "report.html")

        with open(attachment_path, "rb") as attachment_file:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment_file.read())
            encoders.encode_base64(part)  # 加上base64编码，二进制转化为文本，不加报错
            part.add_header(
                "Content-Disposition",
                f"attachment; filename={os.path.basename(attachment_path)}",
            )
        message.attach(part)

        server = smtplib.SMTP_SSL(self.smtp_server, self.smtp_port)
        server.login(self.sender_email, self.sender_password)
        server.sendmail(self.sender_email, self.to_email, message.as_string())
        server.quit()

    # 登录校验，失败会发送邮件
    def login(self):
        r = requests.post(self.login_url, json=self.login_data)
        if r.status_code == 200:
            response_json = r.json()
            if response_json.get("success") == True:
                print("Login successful!")
                return response_json
            else:
                print("Login failed!")
                self.send_email()
                return None
        else:
            print(f"Login request failed with status code: {r.status_code}")
            self.send_email()
            return None


def test_login():
    instance = TestLogin()
    response = instance.login()
    assert response is not None, "Login failed, no response received."
    assert response.get("success") == True, f"Login failed, response: {response}"

if __name__ == '__main__':
    # 生成 HTML 格式的测试报告，并指定报告文件名为 report.html
    pytest.main(['-v', '--html=report.html'])