from django.contrib import admin

from ads.models.ads import Ad

# TODO здесь можно подкючить ваши модели к стандартной джанго-админке
from ads.models.comments import Comment

admin.site.register(Ad)
admin.site.register(Comment)