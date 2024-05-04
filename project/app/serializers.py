from .models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ["id",'username','first_name','last_name','email','password']
