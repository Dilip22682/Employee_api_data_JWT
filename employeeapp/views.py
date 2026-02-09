from django.shortcuts import render
from .models import EmployeeData
from .serializers import EmployeeDataSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated 


# Create your views here.
class EmployeeDetails(viewsets.ModelViewSet):
    queryset=EmployeeData.objects.all()
    serializer_class=EmployeeDataSerializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
