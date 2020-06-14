from django.urls import path
from .views import *

urlpatterns = [
    path('', ProjectList.as_view(), name="project-list"),
    path('project-detail/<int:pk>/', ProjectDetail.as_view(), name="project-detail"),
]
