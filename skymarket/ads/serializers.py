from rest_framework import serializers


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author = serializers.ReadOnlyField(source="author.id")
    ad = serializers.ReadOnlyField(source="ad.id")
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")

    class Meta:
        model = Comment
        fields = ("pk", "text", "created_at", "author_id", "ad_id", "author_first_name", "author_last_name")


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "description")


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author_first_name = serializers.ReadOnlyField(source="author.first_name")
    author_last_name = serializers.ReadOnlyField(source="author.last_name")
    phone = serializers.CharField(max_length=20, source="author.phone", read_only=True)
    author = serializers.ReadOnlyField(source="author.id")

    class Meta:
        model = Ad
        fields = ("pk", "image", "title", "price", "phone", "description", "author_first_name", "author_last_name",  "author_id")
