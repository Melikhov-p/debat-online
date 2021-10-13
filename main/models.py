from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Theme(models.Model):
    name = models.CharField(verbose_name='Тема', max_length=150)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['-id']

class Debat(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, verbose_name='Тема')
    thesis = models.CharField(verbose_name='Тезис', max_length=150)
    members = models.ManyToManyField(User, related_name='debats_users', verbose_name='Участники')

    def __str__(self):
        return self.theme.name

    class Meta:
        verbose_name = 'Дебаты'
        verbose_name_plural = 'Дебаты'
        ordering = ['-id']