# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # 기본 인증 URL 포함
]
