from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tracker import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TasksView, 'tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
