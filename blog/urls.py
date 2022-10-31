from django.urls import path
# 장고 함수인 path와 blog 애플리케이션에서 사용할 모든 view 를 import 함(가져옴)

from.import views

urlpatterns = [
    path("admin/", views.post_list, name='post_list'),
]
