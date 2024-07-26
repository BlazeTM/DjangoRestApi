from django.urls import re_path
from hospitalequipment import views 
 
urlpatterns = [ 
    re_path(r'^api/hospitalequipment$', views.hospital_equipment_list),
    re_path(r'^api/hospitalequipment/(?P<id>\d+)$', views.hospital_equipment_detail, name='id'),
    re_path(r'^api/listofworkersclothes$', views.hospital_equipment_list_of_worker),
     re_path(r'^api/listofworkersclothes/(?P<id>\d+)$', views.hospital_equipment_list_of_worker_detail, name='id'),
    
]