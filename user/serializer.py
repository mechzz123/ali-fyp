
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User

class UserLoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id','email','first_name','address','user_type','contact']


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'first_name', 'last_name', 'user_type', 'contact' , 'address']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user

