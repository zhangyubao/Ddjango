# -*-coding:utf-8-*-
import os
import re
import sys

'''
需要Python2.x版本执行 3.x版本执行报错
'''
rootDir = '/Users/zhangyubao/StudioProjects/Live/Live'


def listdir(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):  # 当前还是一个文件夹
            listdir(file_path)
        else:
            if not('idea' in file_path) and not('build' in file_path) and (file_path.endswith('xml') or file_path.endswith('java')) and not('anim' in file_path) and not('drawable' in file_path) and not('color' in file_path)and not('animator' in file_path):  # 过滤出xml与java文件
                rFile = open(file_path, 'r')
                lineText = rFile.readline()
                newFile = open('key.txt', 'a')
                while lineText:
                    lineText = rFile.readline()
                    strlist = re.findall('"[\x80-\xff]+"', lineText)
                    for text in strlist:
                        newFile.writelines(os.path.basename(
                            file_path) + '---------' + text + '\r')
                rFile.close()
                newFile.close()
                # print(file_path)

listdir(rootDir)
