from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer

from api.models import (User,
                        Request,
                        Invoice)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('username', instance.username)
        instance.save()

        return instance


class MyLoginSerializer(LoginSerializer): # noqa
    email = None


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_login', 'last_activity')


class RequestDetailSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Request
        fields = ('user', 'phone_model', 'description')


class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('request', 'price')


class MasterRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'user', 'phone_model', 'description', 'status')
        read_only_fields = ('id', 'user')


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'user', 'phone_model', 'description', 'status')
        read_only_fields = ('id', 'status', 'user')


class MasterInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'request', 'price', 'paid')
        read_only_fields = ('id', 'paid')


class UserInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('id', 'request', 'price', 'paid')
        read_only_fields = ('id', 'request', 'price')
