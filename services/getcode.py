#! /usr/bin/env python
# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import os,re
from hashlib import md5
class GetCode():
    def __init__(self,git_ssh_url,commit_id,branch=None,tag=None):
        self.git_ssh_url = git_ssh_url
        self.branch = branch or 'master'
        self.commit_id = commit_id
        self.tag = tag
        self.tmp_path = '/apps/dat/deploy/tmp/'
    def getCodebyGit(self):

        mkdir(self.tmp_path) #创建临时代码目录
        project_name = re.split('/', self.git_ssh_url)[1].replace('.git', '')
        # print project_name
        os.system('cd %s && rm -rf %s && git clone %s'%(self.tmp_path,project_name,self.git_ssh_url)) # git clone 项目到 临时代码目录
        # print 'cd %s && rm -rf %s && git clone %s'%(self.tmp_path,project_name,self.git_ssh_url)
        # os.system('cd %s%s'%(self.tmp_path,project_name))
        # print 'cd %s%s'%(self.tmp_path,project_name)
        os.system('cd %s%s && git checkout %s'%(self.tmp_path,project_name,self.commit_id or self.tag) ) #切换到 commit id 版本分支 or tag 版本分支
        # print 'cd %s%s && git checkout %s'%(self.tmp_path,project_name,self.commit_id or self.tag)
        os.system('cd %s && tar cf %s.war %s --remove-files'%(self.tmp_path,project_name,project_name) ) # 把项目 打包成 .war文件
        # print 'cd %s && tar cf %s.war %s --remove-files'%(self.tmp_path,project_name,project_name)
        file_md5 = md5_file('%s%s.war'%(self.tmp_path,project_name)) # 获取打包文件的 MD5 值
        os.system('cd %s && mv %s.war %s.war'%(self.tmp_path,project_name,file_md5)) #把文件以其MD5值命名 后缀为.war
        return file_md5 #返回MD5值 用于下载接口根据提供的MD5值下载文件


'''
    创建目录
'''
def mkdir(dir):
    if exists(dir) is False:
        os.makedirs(dir)

'''
    判断文件是否存在
'''
def exists(file):
    return os.path.exists(file)

def md5_file(name):
    m = md5()
    a_file = open(name, 'rb')    #需要使用二进制格式读取文件内容
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
if __name__ == '__main__':
    url = 'git@git.scm.ppmoney.com:chenjiezheng/test.git'.replace(' ','')
    # print re.split('/',url)[1].split('.')[0]
    # print re.split('/',url)[1].replace('.git','')
    # GetCode(git_ssh_url=url,commit_id='b2a9675f5398ab5d43f299061437ade457c52a2d').getCodebyGit() ##init
    print GetCode(git_ssh_url=url,commit_id='facfdd3ef78700aaea3c42326e1bfb438b23f12e').getCodebyGit() ##latest