from rest_framework import serializers
from . models import *


##############Serializer To make User Friendly It gives HTML form##################
##############Create Api using ApiView#############

class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter Book Title")
    author=serializers.CharField(label="Enter Author Names")
########################################################################


##############Create Api using ModelViewSet#############
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"




