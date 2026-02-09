from django.contrib import admin
from .models import EmployeeData
# Register your models here.

@admin.register(EmployeeData)
class EmployeeDataAdmin(admin.ModelAdmin):
    list_display=['id','emp_name','emp_id','joining_date','mob']