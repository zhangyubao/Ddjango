#!/usr/bin/env python
# coding=utf-8
import os
import sys
'''
# python3 manage.py runserver 8000

项目运行的时候一定要用 python3 mac默认安装的是python2.7 自己安装了Python3.5


本机root用户密码
root@localhost: l3eEBovrdj*r
  
'''

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appsite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
