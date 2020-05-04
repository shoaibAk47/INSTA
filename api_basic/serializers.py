from rest_framework import serializers
from .models import Entity
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Entity

class EntitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model=Entity
        fields=['id','user','image','tags','height','width','created_at','updated_at']

class UserSerializer(serializers.ModelSerializer):
    entities=serializers.PrimaryKeyRelatedField(many=True,queryset=Entity.objects.all())
    class Meta:
        model= User
        fields=['id','username','entities']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','password']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

