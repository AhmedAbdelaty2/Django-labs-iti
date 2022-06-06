from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http.response import JsonResponse,HttpResponseRedirect

my_todos = {
    'one':{'name': 'Gaming', 'priority': 11, 'is_done': False, 'description': 'Play some video games'},
    'two':{'name': 'Feed the cat', 'priority': 2, 'is_done': False, 'description': 'Feet her some cheese'},
    'three':{'name': 'Study', 'priority': 3, 'is_done': False, 'description': 'Try to study'}
}

def todo_list(request):
    return render(request, 'todo/todo.html', context={'my_todos': my_todos})


def todo_detail(request, **kwargs):
    target_todo_name = kwargs.get('todo_name')
    todo_detail = my_todos.get(target_todo_name)
    return render(request, 'todo/todo_detail.html', context={'my_todo': todo_detail})


def delete_todo(request, **kwargs):
    target_todo_name = kwargs.get('todo_name')
    my_target_todo = my_todos.get(target_todo_name)

    if my_target_todo.get('is_done'):
        my_todos.pop(target_todo_name)

    else:
        return render(request, 'todo/todo.html',
                      context={'my_todos': my_todos, 'warning_mgs': "Can't delete unfinished task"})

    return redirect(reverse('todo:list'))


def mark_as_done(request, **kwargs):
    task_key = kwargs.get('todo_name')
    my_target_todo = my_todos.get(task_key)
    my_target_todo['is_done'] = True
    return redirect(reverse('todo:list'))

def add_task(request):
    return render(request, 'todo/add.html')

def insert(request):
    new_task = request.GET
    my_todos[new_task['key']] = {'name':new_task['name'], 'priority':new_task['priority'],'is_done':False,'description':new_task['description']}
    return HttpResponseRedirect (reverse('todo:list'))

def edit(request, **kwargs):
    task_key = kwargs.get('todo_name')
    my_target_todo = my_todos.get(task_key)
    print(my_target_todo)
    return render(request, 'todo/edit.html', context={'my_todo': my_target_todo, 'key':task_key})

def update(request):
    task_to_be_updated = request.GET
    my_todos[task_to_be_updated['key']] = {'name':task_to_be_updated['name'], 'priority':task_to_be_updated['priority'],'is_done':False,'description':task_to_be_updated['description']}
    return HttpResponseRedirect (reverse('todo:list'))

