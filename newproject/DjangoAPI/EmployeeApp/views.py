from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departement,Employees
from EmployeeApp.serializers import DepartementSerializer,EmployeeSerializer

# Create your views here.

def departementApi(request,id=0):
    if request.method=='GET':
        departements = Departement.objects.all()
        departements_serializer=DepartementSerializer(departement,many=True)
        return JsonResponse(departements_serializer.data,safe=False)
    elif request.method=='POST':
        departement_data=JSONParser().parse(request)
        departments_serializer=DepartementSerializer(data=departement_data) 
        if departements_serializer.is_valid():
            departements_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        departement_date=JSONParser().parse(request)
        departement=Departements.objects.get(DepartementId=departement_data['DepartementId'])
        departements_serializer=DepartementSerializer(departement,date=departement_data)
        if departements_serializer.is_valid():
            departements_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        departement=Departement.objects(Departement=id)
        departement.delete()
        return JsonResponse('Delete Successfully',safe=False)        
        
