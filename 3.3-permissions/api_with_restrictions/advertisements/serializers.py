from django.contrib.auth.models import User
from rest_framework import serializers
from advertisements.models import Advertisement
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at',)
        read_only_fields = ['creator']

    def create(self, validated_data):
        if len(Advertisement.objects.filter(creator=self.context["request"].user, status='OPEN')) > 10:
            raise ValidationError('Разрешено не более 10 объявлений')

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        return data
