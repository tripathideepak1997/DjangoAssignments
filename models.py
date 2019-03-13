from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    salary = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    reporting_manager = models.ForeignKey('self',null=True,on_delete=models.CASCADE)
    DESIGNATION = (
        ('Developer','DEVELOPER'),
        ('Trainee','Trainee Engineer'),
        ('SE','Software Engineer'),
        ('SA','System Analyst'),
        )

    designation = models.CharField(max_length=50,choices=DESIGNATION)

