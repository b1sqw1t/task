from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор')
    text   = models.TextField()
    created = models.DateTimeField(auto_now_add=True,auto_now=False,verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=False,auto_now=True,verbose_name='Изменен')