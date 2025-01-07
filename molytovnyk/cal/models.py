from django.conf import settings
from django.db import models
from django.utils import timezone
# from datetime import timedelta, date


class Holiday(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Назва свята")
    description = models.TextField(blank=True, verbose_name="Про свято")
    date = models.DateField(verbose_name="дата святкування")
    is_fixed = models.BooleanField(default=True, verbose_name="Фіксована дата")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата останнього оновлення")


    # def should_announce(self):
    #     """
    #     Перевіряє чи потрібно анонсувати свято за день до його настання
    #     """
    #     today = date.today()
    #     return today == self.date - timedelta(days=1)

    class Meta:
        verbose_name = "Свято"
        verbose_name_plural = "Свята"
        ordering = ["date"]

    def __str__(self):
        return self.name