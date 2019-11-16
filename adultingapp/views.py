from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializers import AdultingTaskSerializer,CategorySerializer
from .models import AdultingTask,Category
# Create your views here.

class AdultingTask(viewsets.ModelViewSet):       
      serializer_class = AdultingTaskSerializer    
      queryset = AdultingTask.objects.all()             
class Category(viewsets.ModelViewSet):       
      serializer_class = CategorySerializer    
      queryset = Category.objects.all()  
      

