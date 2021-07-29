from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drfapp.serializers import *
from drfapp.models import *


class TestView(APIView):
    
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        student1 = qs.first()
        serializer = StudentSerializer(student1)
        data = {
            'username': 'admin',
            'years_active': 10
        }
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
