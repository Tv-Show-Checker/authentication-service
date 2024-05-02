from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validate_password(validated_data.get('password'))
        user = get_user_model().objects.create_user(**validated_data)
        return user
