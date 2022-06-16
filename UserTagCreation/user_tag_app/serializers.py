from dataclasses import fields
from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields='__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    conform_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields=['username','email','password','conform_password']

class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields=['email','password']

class UserTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Tag
        exclude =("timestamp",)

class DetailUserTagSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('is_title')
    user = serializers.SerializerMethodField('is_user')
    def is_title(sef,obj):
        if obj.title:
            return obj.title.title
        return None
    def is_user(sef,obj):
        if obj.user:
            return obj.user.username
        return None

    class Meta:
        model = User_Tag
        fields=["title","content","user","timestamp"]

class UpdateUserTagSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField('is_title')
    user = serializers.SerializerMethodField('is_user')
    def is_title(sef,obj):
        if obj.title:
            return obj.title.title
        return None
    def is_user(sef,obj):
        if obj.user:
            return obj.user.username
        return None

    class Meta:
        model = User_Tag
        fields=["title","content","user"]
