from . import views  # 导入views模块
from django.urls import path

urlpatterns = [
    path("", views.index, name="index")  # 配置当访问index/时去调用views下的index方法
]