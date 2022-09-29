from django.conf import settings
from django.db import models

from ads.models.ads import Ad
from users.models import User


class Comment(models.Model):
    # TODO добавьте поля модели здесь
    text = models.CharField(blank=True, max_length=500)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания объявления",
        help_text="Введите время создания объявления",
        null=True
    )
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'