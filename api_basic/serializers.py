from rest_framework import serializers
from .models import Entity
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Entity, EntityTags

class ShowTagSerializer(serializers.ModelSerializer):
    class Meta:
        model=EntityTags
        fields=['id','title','relentity']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=EntityTags
        fields=['title']

class EntitySerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    tags_list=TagSerializer(many=True)
    class Meta:
        model=Entity
        fields=['id','user','image','tags_list','height','width','created_at','updated_at']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags_list')
        entity = Entity.objects.create(**validated_data)
        for tags_data in tags_data:
            try:
                b=EntityTags.objects.get(title=tags_data['title'], user=validated_data['user'])
                b.relentity.add(entity)
                b.save()
            except EntityTags.DoesNotExist:
                a=EntityTags.objects.create(user=validated_data['user'], **tags_data)
                a.save()
                a.relentity.add(entity)
                a.save()
        return entity

class UserSerializer(serializers.ModelSerializer):
    entities=serializers.PrimaryKeyRelatedField(many=True,queryset=Entity.objects.all())
    class Meta:
        model= User
        fields=['id','username','entities']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.filter())])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','password']

    def create(self, validated_data):
        a=User.objects.filter(email__iexact=validated_data['email'])
        b=User.objects.filter(username__iexact=validated_data['username'])
        if a:
            raise serializers.ValidationError("email already exist")
        elif b:
            raise serializers.ValidationError("username already exist")
        else:
            user = super().create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user