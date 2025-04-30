from django.http import JsonResponse
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_todo(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = data.get('task')
        due_date = data.get('due_date')
        completed = data.get('completed')
        todo = Todo.objects.create(task=task,due_date=due_date,completed=completed)
        response = JsonResponse({
            'id':todo.id,
            'task':todo.task,
            'due_date':todo.due_date,
            'completed':todo.completed,
        },status=201)
        return response

@csrf_exempt
def get_all_todos(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        todos_list = list(todos.values())
        response = JsonResponse(todos_list, safe=False, status=200)
        return response

@csrf_exempt
def get_todo(request, id):
    if request.method == 'GET':
        todo = Todo.objects.get(id=id)
        response = JsonResponse({
            'id':todo.id,
            'task':todo.task,
            'due_date':todo.due_date,
            'completed':todo.completed,
        },status=200)
        return response

@csrf_exempt
def update_todo(request, id):
    if request.method == 'PUT':
        todo = Todo.objects.get(id=id)
        data = json.loads(request.body)
        todo.task = data.get('task')
        todo.due_date = data.get('due_date')
        todo.completed = data.get('completed')
        todo.save()
        response = JsonResponse({
            'id':todo.id,
            'task':todo.task,
            'due_date':todo.due_date,
            'completed':todo.completed,
        },status=200)
        return response

@csrf_exempt
def delete_todo(request, id):
    if request.method == 'DELETE':
        todo = Todo.objects.get(id=id)
        task = todo.task
        todo.delete()
        response = JsonResponse({'message':f'id:{id} task:{task} を削除しました。'},status=200, json_dumps_params={'ensure_ascii': False})
        return response
    