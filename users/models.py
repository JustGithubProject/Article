from django.db import models


class Register(models.Model):
    """Model for reg"""
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Регистрация"
