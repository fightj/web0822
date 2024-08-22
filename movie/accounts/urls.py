# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),  # 기본 인증 URL 포함
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # 로그아웃 후 홈으로 리디렉션
]
