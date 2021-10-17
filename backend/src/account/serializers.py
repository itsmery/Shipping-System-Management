from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Profile

User = get_user_model()


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=100, required=True)
    password = serializers.CharField(max_length=100, required=True)

    def validate_email(self, value):
        if not self.context.get("login", False):
            user = User.objects.filter(email__iexact=value).exists()

            if user:
                raise serializers.ValidationError("Email is invalid")

            return value

    def save(self):
        email = self.validated_data["email"]
        password = self.validated_data["password"]

        user = User.objects.create_user(email=email, password=password)
        user.set_password(password)
        user.save()

        print("Create successfully", email, password)

        return user


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    isAdmin = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        exclude = ("user", "id", "dateCreated")

    def get_email(self, obj):
        return obj.user.email

    def get_isAdmin(self, obj):
        return obj.user.is_admin

    def update(self, instance, validated_data):
        instance.fullName = self.validated_data.get("fullName", instance.fullName)
        instance.phone = self.validated_data.get("phone", instance.phone)
        instance.address = self.validated_data.get("address", instance.address)
        instance.gender = self.validated_data.get("gender", instance.gender)
        instance.dateOfBirth = self.validated_data.get(
            "dateOfBirth", instance.dateOfBirth
        )
        instance.provinceId = self.validated_data.get("provinceId", instance.provinceId)
        instance.districtId = self.validated_data.get("districtId", instance.districtId)
        instance.subDistrictId = self.validated_data.get(
            "subDistrictId", instance.subDistrictId
        )

        instance.save()

        return instance
