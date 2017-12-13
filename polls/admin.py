from django.contrib import admin
from .models import Question, Choice

# Register your models here.

# 保证在创建Question的时候添加


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    """docstring for QuestionAdmin"""
    # fields = ['publish_date', 'question_text']

    # 添加标题描述
    # fieldsets = [('这是问题', {'fields': ['question_text']}),
    #              ('这是问题的发布日期', {'fields': ['publish_date']})]

    # 给字段添加制定的Html样式
    fieldsets = [('这是问题', {'fields': ['question_text']}),
                 ('这是问题的发布日期', {'fields': ['publish_date'], 'classes':['collapse']})]

    inlines = [ChoiceInline]

    # 使用list_display 可以控制页面针对问题显示的标题
    list_display = ('question_text', 'publish_date', 'was_published_recently')

    # list_filter使用来做筛选
    list_filter = ['publish_date']

    # search_fields用来做搜索    还有一些其他功能 Change list pagination、search
    # boxes、filters、date-hierarchies和column-header-ordering
    search_fields = ['question_text']

# 注册之后再管理后台会出现操作界面
admin.site.register(Question, QuestionAdmin)
# 注册Choice的第一种方式
# admin.site.register(Choice)

# 现在要求在创建Question的时候就要添加Choice
