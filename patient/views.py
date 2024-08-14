from django.shortcuts import render
from rest_framework import viewsets
from .import serializers
from .import models
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer
    
class UserRegistrationApiView(APIView):
    serializer_class = serializers.PatientRegisterSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            return Response("Done")
        return Response(serializer.errors)