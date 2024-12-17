from . import views  # 导入views模块
from django.urls import path

urlpatterns = [
    path("", views.index, name="sentiment")
]