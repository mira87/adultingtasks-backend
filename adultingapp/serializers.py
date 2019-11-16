from rest_framework import serializers
from .models import AdultingTask,Category

class AdultingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= AdultingTask
        fields=('title','taskpic','summary','details','category','id')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=('title','id')