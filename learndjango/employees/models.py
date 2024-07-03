from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    startDate = models.DateField()
    salary = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Employees'