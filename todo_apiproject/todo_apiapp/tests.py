from django.test import TestCase
from .models import Todo

class TodoDetailViewTest(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(
            task='テストデータ',
            due_date='2025-05-06'
        )
        self.valid_url = f'/api/todos/{self.todo.id}/'
        self.invalid_url = '/api/todos/9999/'

    def test_get_existing_todo(self):
        """
        GETリクエスト時、対象のidと紐づくタスクが存在する場合ステータスコード200を返す
        """
        response = self.client.get(self.valid_url)
        self.assertEqual(response.status_code, 200)
    
    def test_get_nonexisting_todo(self):
        """
        GETリクエスト時、対象のidと紐づくタスクが存在しない場合ステータスコード404を返す
        """
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.status_code, 404)
    
    def test_get_404_msg(self):
        """
        GETリクエスト時、対象のidと紐づくタスクが存在しない場合、{'detail':'Not found'}を返す
        """
        response = self.client.get(self.invalid_url)
        self.assertEqual(response.json(), {'detail':'Not found'})

    def test_get_endpoint_rejects_post(self):
        """
        GET専用エンドポイントにPOSTリクエストを送信した場合、ステータスコード405を返す
        """
        response = self.client.post(self.valid_url)
        self.assertEqual(response.status_code, 405)

    def test_get_correct_id(self):
        """
        GETリクエスト成功時、期待するidを返す
        """
        response = self.client.get(self.valid_url)
        self.assertEqual(response.json()['id'], self.todo.id)

    def test_get_correct_task(self):
        """
        GETリクエスト成功時、期待するtaskを返す
        """
        response = self.client.get(self.valid_url)
        self.assertEqual(response.json()['task'], self.todo.task)

    def test_get_correct_due_date(self):
        """
        GETリクエスト成功時、期待するdue_dateを返す
        """
        response = self.client.get(self.valid_url)
        self.assertEqual(response.json()['due_date'], self.todo.due_date)

    def test_get_correct_completed(self):
        """
        GETリクエスト成功時、期待するcompletedを返す
        """
        response = self.client.get(self.valid_url)
        self.assertEqual(response.json()['completed'], self.todo.completed)
