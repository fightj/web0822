from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),  # 추가된 URL 패턴
    # 다른 URL 패턴들...
]
