from django.contrib import admin


# Register your models here.
# 导入我们要注册的模型Topic
from learning_logs.models import Topic
# 让Django通过管理网站管理我们的模型
admin.site.register(Topic)