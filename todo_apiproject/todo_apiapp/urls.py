from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.get_all_todos),
    path('todos/<int:id>/', views.get_todo),
    path('todos/create/', views.create_todo),
    path('todos/update/<int:id>/', views.update_todo),
    path('todos/delete/<int:id>/', views.delete_todo),
]
