from django.db import models
from employees.models import Employee

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    employees = models.ManyToManyField(Employee, related_name='projects', blank=True)

    def __str__(self):
        return self.name
