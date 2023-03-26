from django.urls import path
from .import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('api/todo_list/', views.todo_list, name='todo_list'),
    path('api/todo_detail/<str:pk>', views.todo_detail, name='todo_detail'),
    path('api/todo_create/', views.todo_create, name='todo_create'),
    path('api/todo_update/<str:pk>', views.todo_update, name='todo_update'),
    path('api/todo_delete/<str:pk>', views.todo_delete, name='todo_delete'),
]
