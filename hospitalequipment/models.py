from django.db import models

# Create your models here.
class Employes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=100)
    surname = models.CharField(blank=False, max_length=100)
    ward = models.CharField(blank=False, max_length=100)

class EmployesClothes(models.Model):
    id = models.AutoField(primary_key=True)
    id_of_employe = models.IntegerField()
    description = models.CharField(blank=False, max_length=999)
    type_of_action = models.CharField(blank=False, max_length=999)
    created = models.DateTimeField(auto_now_add=True)