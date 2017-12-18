"""appsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

'''
url() 函数解释
第一个参数：对于http://www.example.com/myapp/请求，URLconf 将查找myapp/。对于http://www.example.com/myapp/?page=3请求，URLconf 也将查找myapp/。
第二个参数：当Django找到一个匹配的正则表达式时，它就会调用view参数指定的视图函数
第三个参数：任何关键字参数都可以以字典形式传递给目标视图。 我们在这个教程里不用Django的这个功能
第四个参数：命名你的URL。 这样就可以在Django的其它地方尤其是模板中，通过名称来明确地引用这个URL。 这个强大的特性可以使你仅仅修改一个文件就可以改变全局的URL模式
'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'^west/', include('west.urls')),
]
