from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):

    TASK_TYPE = [
        ('DAILY', 'Daily'),
        ('WEEKLY', 'Weekly'),
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
        ('BUCKETLIST', 'BucketList'),
    ]

    task_title = models.CharField(max_length=50)
    task_description = models.CharField(max_length=200)
    task_type = models.CharField(
        max_length=50,
        choices=TASK_TYPE,
        default=TASK_TYPE[0][0],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_progress =  models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasks'
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ['-updated_at']

    def __str__(self):
        return self.task_title
