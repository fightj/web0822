# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', include('accounts.urls')),  # 회원가입 URL 추가
    path('accounts/', include('accounts.urls')),  # 로그인 URL 추가
    path('', accounts_views.home, name='home'),  # 홈 페이지 URL
]
