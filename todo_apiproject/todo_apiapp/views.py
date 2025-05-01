from django.http import JsonResponse
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
import json

# レスポンス作成を共通化
def create_response(todo, status):
    response = JsonResponse({
        'id':todo.id,
        'task':todo.task,
        'due_date':todo.due_date,
        'completed':todo.completed,
    }, status=status)
    return response

# 特定のIDのTodoタスクを取得するAPIエンドポイント
@csrf_exempt
def todo_detail(request, id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return JsonResponse({'detail':'Not found'}, status=404)
        response = create_response(todo, 200)
        return response
    elif request.method == 'PUT':
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return JsonResponse({'detail':'Not found'}, status=404)
        data = json.loads(request.body)
        todo.task = data.get('task')
        todo.due_date = data.get('due_date')
        todo.completed = data.get('completed')
