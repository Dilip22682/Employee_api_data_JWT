from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=100)
    joining_date = models.DateField()  
    mob = models.CharField(max_length=15)

    def __str__(self):
        return self.emp_name
  
