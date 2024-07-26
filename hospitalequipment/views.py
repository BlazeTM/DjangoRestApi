from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from hospitalequipment.models import Employes, EmployesClothes
from hospitalequipment.serializers import EmployesSerializer, EmployesClothesSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def hospital_equipment_list(request):
    if request.method == 'GET':
        tutorials = Employes.objects.all()
        
        id = request.query_params.get('id', None)
        if id is not None:
            tutorials = tutorials.filter(id__icontains=id)
        
        tutorials_serializer = EmployesSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = EmployesSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Employes.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def hospital_equipment_detail(request, id):
    try: 
        table = Employes.objects.get(id=id) 
    except table.DoesNotExist: 
        return JsonResponse({'message': 'The Employes does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = EmployesSerializer(table) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = EmployesSerializer(Employes, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        Employes.delete() 
        return JsonResponse({'message': 'Employes was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST', 'DELETE'])
def hospital_equipment_list_of_worker(request):
    if request.method == 'GET':
        tutorials = EmployesClothes.objects.all()
        
        id = request.query_params.get('id', None)
        if id is not None:
            tutorials = tutorials.filter(id__icontains=id)
        
        tutorials_serializer = EmployesClothesSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = EmployesClothesSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = EmployesClothes.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)        

@api_view(['GET', 'PUT', 'DELETE'])
def hospital_equipment_list_of_worker_detail(request, id):
    try: 
        table = EmployesClothes.objects.get(id=id) 
    except table.DoesNotExist: 
        return JsonResponse({'message': 'The Employes does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = EmployesClothesSerializer(table) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = EmployesClothesSerializer(EmployesClothes, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        EmployesClothes.delete() 
        return JsonResponse({'message': 'Employes was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 