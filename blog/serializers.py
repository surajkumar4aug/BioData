from rest_framework import serializers
from .models import Post, Comment, Like, Otp
from django.contrib.auth.models import User
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class OtpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = '__all__'
