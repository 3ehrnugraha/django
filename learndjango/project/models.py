from django.db import models
from employees.models import Employee

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    employees = models.ManyToManyField(Employee, related_name='projects', blank=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(Employee, related_name='tasks', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
