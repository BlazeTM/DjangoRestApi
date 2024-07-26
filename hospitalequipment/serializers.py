from rest_framework import serializers 
from hospitalequipment.models import Employes, EmployesClothes

 
class EmployesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employes
        fields = ('id',
                  'name',
                  'surname',
                  'ward')
        
         
class EmployesClothesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = EmployesClothes
        fields = ('id',
                  'id_of_employe',
                  'description',
                  'type_of_action',
                  'created')