from django.http import JsonResponse
from .models import Todo
import json

# レスポンス作成を共通化
def todo_response(todo, status):
    response = JsonResponse({
        'id':todo.id,
        'task':todo.task,
        'due_date':todo.due_date,
        'completed':todo.completed,
    }, status=status)
    return response

# 特定のIDのTodoタスクを取得するAPIエンドポイント
def todo_detail(request, id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=id)
        except Todo.DoesNotExist:
            return JsonResponse({'detail':'Not found'}, status=404)
        response = todo_response(todo, 200)
        return response
    else:
        return JsonResponse({'detail':'Method Not Allowed'}, status=405)

def todos(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        todo_list = list(todos.values())
        response = JsonResponse(todo_list, safe=False, status=200)
        return response
    elif request.method == 'POST':
        data = json.loads(request.body)
        task = data.get('task')
        due_date = data.get('due_date')
        todo = Todo.objects.create(task=task, due_date=due_date, completed=False)
        response = todo_response(todo, 201)
        return response
