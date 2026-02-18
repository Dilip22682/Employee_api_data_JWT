from rest_framework import serializers
from .models import EmployeeData

class EmployeeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeData
        fields='__all__'