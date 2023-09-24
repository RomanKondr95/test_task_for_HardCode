from rest_framework import serializers
from .models import *

class LessonSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Lesson
        fields = ('title','duraton','last_viewed','user','status')
    def get_user(self, obj):
        return obj.user.username if obj.user else None

class ProductLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'duraton', 'last_viewed', 'user','status')

