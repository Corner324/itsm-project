from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from .models import CustomUser 

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise ValidationError("Пользователь с таким именем уже существует.")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Пользователь с таким email уже зарегистрирован.")
        return value

    def create(self, validated_data):
        role = validated_data.pop('role', 'employee')  # Роль по умолчанию
        user = CustomUser.objects.create_user(**validated_data, role=role)
        return user


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()  # Используем кастомную модель
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Добавляем дополнительные данные в токен
        token['username'] = user.username
        token['role'] = user.role
        return token

    def validate(self, attrs):
        try:
            data = super().validate(attrs)
        except AuthenticationFailed as e:
            raise AuthenticationFailed("Неверное имя пользователя или пароль.")

        data['username'] = self.user.username
        data['role'] = self.user.role
        return data
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
