from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from .serializers import CustomUserSerializer

from .models import CustomUser


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password", "email", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise ValidationError("Пользователь с таким именем уже существует.")
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Пользователь с таким email уже зарегистрирован.")
        return value

    def create(self, validated_data):
        role = validated_data.pop("role", "employee")
        user = CustomUser.objects.create_user(**validated_data, role=role)
        return user


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username
        token["role"] = user.role
        return token

    def validate(self, attrs):
        try:
            data = super().validate(attrs)
        except AuthenticationFailed as e:
            raise AuthenticationFailed("Неверное имя пользователя или пароль.")

        data["username"] = self.user.username  # type: ignore
        data["role"] = self.user.role  # type: ignore
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class AdminDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:

            admin = CustomUser.objects.get(role="admin")
            return Response({"id": admin.id, "username": admin.username})  # type: ignore
        except CustomUser.DoesNotExist:
            return Response({"detail": "Администратор не найден."}, status=404)


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


class UserListView(APIView):
    """
    Возвращает список всех пользователей, исключая администратора (или других фильтраций при необходимости).
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.exclude(id=request.user.id)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
