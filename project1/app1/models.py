from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_marks = models.FloatField()
    student_address = models.CharField(max_length=200)
