from django.db import models


class News(models.Model):
    """Model for NEWS"""
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"