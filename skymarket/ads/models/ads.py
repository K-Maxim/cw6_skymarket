from django.conf import settings
from django.db import models


class Ad(models.Model):
    # TODO добавьте поля модели здесь
    title = models.CharField(max_length=50, null=True)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="images/",
        verbose_name="фото",
        help_text="Разместите фото для объявления",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title




