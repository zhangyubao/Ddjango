from django.db import models

# Create your models here.


# 问题实体类
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date publish')

    def _str_(self):
        return self.question_text


# 投票实体类
class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, default='')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def _str_(self):
        return self.choice_text + str(self.votes)


'''
注意：模型定义完成需要执行以下命令通知Django 模型已经改变
python manage.py makemigrations polls


请记住实现模型变更的三个步骤：

修改你的模型（在models.py文件中）
运行python manage.py makemigrations appname，为这些修改创建迁移文件
运行python manage.py migrate ，将这些改变更新到数据库中


Django 超级管理员及密码：
用户名：admin
密码 ：zyb123456


'''
