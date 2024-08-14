from rest_framework import serializers
from .import models
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'

class PatientRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','confirm_password']
        def save(self):
            username = self.validated_data["username"]
            email = self.validated_data["email"]
            password = self.validated_data["password"]
            password2 = self.validated_data["confirm_password"]
            
            if password != password2:
                raise serializers.ValidationError({"error":"Password doesn't matched!"})
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({"error":"Email already exist!!"})
            account = User(username=username, email=email)
            account.set_password(password)
            account.save()
            return account