from django.db import models

# Create your models here.


class Person(object):
    """docstring for Person"""
    GENDER = ((1, 'Male'), (2, 'Female'))
    '''
    相当于java中的枚举类  在此为字段值提供选项(choices)
    default字段的默认值
    help_text表单部件额外显示的帮助内容
    primary_key如果为True，那么这个字段就是模型的主键
    unique如果该值设置为 True, 这个数据字段在整张表中必须是唯一的
    '''

    first_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER, default=GENDER[0])

    '''
    除ForeignKey、ManyToManyField 和 OneToOneField 之外，
    每个字段类型都接受一个可选的位置参数（在第一的位置） —— 字段的自述名。
    如果没有给定自述名，Django 将根据字段的属性名称自动创建自述名 —— 将属性名称的下划线替换成空格。


    ForeignKey、ManyToManyField 和 OneToOneField 第一个参数必须是模型类
    使用verbose_name关键字参数才能指定自述名
    '''
    second_name = models.CharField('this is second name', max_length=30)


'''
以下两个类演示多余多关系通过through制定一个中介模型;

如果有超过两个外键，同样你必须像上面一样指定through_fields，否则将引发一个验证错误。

使用中介模型定义与自身的多对多关系时，你必须设置 symmetrical=False

使用中介模型后 不能使用普通多对多的add create remove方法创建和删除管理关系 必须使用创建中介模型的实例的方法  但是clear方法是可用的
'''


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person)
    group = models.ForeignKey(Group)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    # def save(self, *args, **kwargs):
    # 覆盖了自带的save方法 做一些事情  调用父类方法保证数据保存到数据库
    # super(Membership, self).save(*args, **, kwargs)


'''
模型元数据是“任何不是字段的数据”，
排序选项（ordering），
数据库表名（db_table）,
可读的单复数名称（verbose_name 和verbose_name_plural）。
在模型中添加class Meta是完全可选的，所有选项都不是必须的。

'''

'''
抽象类需要在Model 中的Meta类设置 abstract=True Django把你在基类内部定义的 Meta 类作为一个属性使其可用


related_name：当你在(且仅在)抽象基类中使用related_name 时，如果想绕过这个问题，名称中就要包含'%(app_label)s'和 '%(class)s'
'%(class)s'会替换为子类的小写加下划线格式的名称，字段在子类中使用。
'%(app_label)s'会替换为应用的小写加下划线格式的名称，应用包含子类。每个安装的应用名称都应该是唯一的，而且应用里每个模型类的名称也应该是唯一的，所以产生的名称应该彼此不同


ChildA.m2m 字段的反向名称是 common_childa_related，而 ChildB.m2m 字段的反向名称是 rare_childb_related。
这取决于你如何使用'%(class)s' 和'%(app_label)s来构造你的反向名称。如果你没有这样做，Django 就会在验证 model (或运行 migrate) 时抛出错误


如果你没有在抽象基类中为某个关联字段定义 related_name 属性，那么默认的反向名称就是子类名称加上'_set'
'''
from django.db import models


class Base(models.Model):
    m2m = models.ManyToManyField(
        OtherModel, related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass
# 假设下面这个类在另一个应用中

# from common.models import Base


class ChildB(Base):
    pass


'''
代理继承
'''


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):

    class Meta:
        proxy = True
        ordering = ['']
        # 这里所有的Meta属性都可以使用

    def do_something(self):
        # ...
        pass
