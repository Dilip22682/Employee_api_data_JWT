from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    emp_name=models.CharField(max_length=100)
    emp_id=models.IntegerField()
    joining_date = models.DateField()   # ✅ ADD THIS
    mob = models.CharField(max_length=15)

    def __str__(self):
        return self.emp_name
  
