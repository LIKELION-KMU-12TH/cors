from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListAPIView.as_view()), # get - 블로그 리스트 조회
    path('<int:blog_id>/', views.BlogDetailAPIView.as_view()), # post - 블로그 작성
]