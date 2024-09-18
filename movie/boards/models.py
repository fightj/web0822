from django.db import models
from django.conf import settings  # 커스텀 유저 모델을 참조하기 위한 import

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 커스텀 유저 모델을 참조
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
