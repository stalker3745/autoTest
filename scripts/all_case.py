# coding:utf-8
import  pytest
import os

path=os.path.join(os.getcwd(),"")
case_path1=os.path.join(path,"")
report_path=os.path.join(os.path.join(os.getcwd()),"report")

def all_case():
    discover=pytest.main([case_path1,"-s"])
    return discover

if __name__== "__main__":
    all_case()
