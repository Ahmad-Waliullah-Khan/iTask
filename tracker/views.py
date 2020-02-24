from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TasksSerializer
from .models import Tasks

class TasksView(viewsets.ModelViewSet):
  serializer_class = TasksSerializer
  queryset = Tasks.objects.all()
