from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todos),
    path('todos/<int:id>/', views.todo_detail),
]
