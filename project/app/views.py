
from .models import  *
from .serializers import *
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status

@api_view(['GET', 'POST'])  
def userList(request): 
    if request.method=='GET':
        student = StudentModel.objects.all() 
        serializer=UserSerializer(student,many=True)
        return Response(serializer.data) 
    
    elif request.method=='POST':
        serializer=UserSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)

@api_view(['GET', 'PUT','DELETE']) 
def userDetails(request,pk): 
    if request.method=='GET': 
        try: 
            student=StudentModel.objects.get(pk=pk) 
        except StudentModel.DoesNotExist: 
            return Response({'error':'Detail not found'},status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(student) 
        return Response(serializer.data) 
    elif request.method=='PUT': 
        student=StudentModel.objects.get(pk=pk) 
        serializer = UserSerializer(student,data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors) 
    elif request.method=='DELETE': 
        student=StudentModel.objects.get(pk=pk) 
        student.delete() 
        return Response({'error':"Data deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

