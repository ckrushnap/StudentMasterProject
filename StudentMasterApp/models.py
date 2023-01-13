from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=50)
    UserName = models.CharField(max_length=50)
    UserEmail=models.CharField(max_length=50)
    Password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Name}'


class Master(models.Model):
    Name = models.CharField(max_length=50)
    UserName = models.CharField(max_length=50)
    UserEmail=models.CharField(max_length=50)
    Password = models.CharField(max_length=50)


class Task(models.Model):
    Left = models.CharField(max_length=50)
    Right = models.CharField(max_length=50)
    Operator = models.CharField(max_length=50)
    Complete = models.BooleanField(default=False)
    Student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
