from rest_framework import serializers
from API.models import CUser, Vendor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CUser
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["id", "username", "password", "email" , "users"]
        extra_kwargs = {"password": {"write_only": True}}