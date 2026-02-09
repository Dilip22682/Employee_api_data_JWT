from rest_framework import serializers
from .models import EmployeeData

class EmployeeDataSerializer(serializers.ModelSerializer):
    class meta:
        model=EmployeeData
        fields='__all__'