from django.urls import path
from .views import todo_list, todo_detail, delete_todo, mark_as_done, add_task, insert, edit, update

app_name = 'todo'

urlpatterns = [
    path('list', todo_list, name='list'),
    path('update', update, name='update'),
    path('add', add_task, name='add'),
    path('edit/<str:todo_name>', edit, name='edit'),
    path('my-todo-detail/<str:todo_name>', todo_detail, name='detail'),
    path('done/<str:todo_name>', mark_as_done, name='done'),
    path('delete/<str:todo_name>', delete_todo, name='delete'),
    path('insert', insert, name='insert'),
]

