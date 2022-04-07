from rest_framework immport serializers
from EmployeeApp.models import Departement, Employees

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departements
        fields=('DepartementId','DepartementName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Departement','DateOfJoining','PhotofileName')