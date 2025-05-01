from django.urls import path
from . import views

urlpatterns = [
    path('todos/<int:id>/', views.todo_detail),
]
