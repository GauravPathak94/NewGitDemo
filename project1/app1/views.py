from django.shortcuts import render
from .models import Student
from .Serializer import StudentSerializer
from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import status

# Create your views here.
class Studentdetails(APIView):
    def get(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class StudentInfo(APIView):
    def get(self, request, id):
        try:
            stu = Student.objects.get(pk = id)
        except Student.DoesNotExist:
            msg = {'msg': 'Record does NOT FOUND'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(stu)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            stu = Student.objects.get(pk = id)
        except Student.DoesNotExist:
            msg = {'msg':'Record does NOT FOUND'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            stu = Student.objects.get(pk = id)
        except Student.DoesNotExist:
            msg = {'msg': 'Record does NOT FOUND'}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
