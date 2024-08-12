from django.shortcuts import render
from rest_framework import viewsets
from .import serializers
from .import models
# Create your views here.

class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer