'''
读文件相关的方法
'''
import configparser
import os

import yaml


def get_project_path():
    # C:\ApiAutoTest53\zonghe\
    # 根据当前文件的路径（__file__），获取工程路径。
    cf = os.path.realpath(__file__)  # fileRead.py
    cd = os.path.dirname(cf)  # caw
    cd = os.path.dirname(cd)  # zonge
    return cd + "\\"


def read_ini(path, key):
    '''
    读取配置文件，获取key对应的value
    :param path:  配置文件所在的路径
    :param key:  要读取的key
    :return:  key对应的value
    '''
    path = get_project_path() + path
    print(path)
    cp = configparser.ConfigParser()  # 创建一个实例
    cp.read(path, encoding="utf-8")
    return cp.get("env", key)  # env是ini中的[env]，也就是section

def read_yaml(path):
    path = get_project_path() + path
    with open(path, mode="r", encoding='utf-8') as f:
        c = f.read()  # 读取文件内容
        # yaml  模块
        # Loader 可选参数
        # pip install pyyaml
        return  yaml.load(c, Loader=yaml.FullLoader)

# 测试代码，用完可以删除
if __name__ == '__main__':  # 写个main敲回车，自动补齐
    a = read_yaml("data_case/register_fail.yaml")
    print(a)  # List

    # 绝对路径导致脚本的可移植性不好。通过代码获取C:\ApiAutoTest53\zonghe\
    a = read_ini(r"data_env\env.ini", "url")
    print(a)
    b = read_ini(r"data_env\env.ini", "db")
    print(b)
    print(type(b))  # <class 'str'>
    # 字符串怎么转字典？
    c = eval(b)  # 百度下
    print(type(c))   # <class 'dict'>
    print(c)
