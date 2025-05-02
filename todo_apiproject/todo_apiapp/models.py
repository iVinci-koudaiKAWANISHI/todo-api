from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=100)
    due_date = models.DateField(null=True,blank=True)
    completed = models.BooleanField(default=False)
