from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ('task_title', 'task_type', 'created_at', 'updated_at', 'user', 'in_progress')
