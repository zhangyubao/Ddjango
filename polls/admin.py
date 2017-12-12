from django.contrib import admin
from .models import Question

# Register your models here.
# 注册之后再管理后台会出现操作界面
admin.site.register(Question)
