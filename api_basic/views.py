from .models import Entity, EntityTags
from .serializers import RegisterSerializer, EntitySerializer, UserSerializer, ShowTagSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedAndOwner
from django.http import Http404
from rest_framework.decorators import permission_classes

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Insta')

@api_view(['POST'])
def RegisterView(request):
    serializer=RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

@api_view(['GET'])
def ShowUser(request):
    user=User.objects.all()
    serializer=RegisterSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShowEntity(request):
    user=User.objects.all()
    serializer=UserSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllTags(request):
    tags=EntityTags.objects.filter(user=request.user)
    serializer=ShowTagSerializer(tags,many=True)
    return Response(serializer.data)

class EntityAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        entities=Entity.objects.filter(user=request.user)
        serializer=EntitySerializer(entities,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=EntitySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

class EntityDetails(APIView):
    permission_classes=[IsAuthenticatedAndOwner]
    def get_object(self,id):
        try:
            obj=Entity.objects.get(id=id)
            self.check_object_permissions(self.request, obj)
            return obj
        except Entity.DoesNotExist:
            raise Http404

    def get(self, request, id):
        entity=self.get_object(id)
        serializer=EntitySerializer(entity)
        return Response(serializer.data)

    def put(self, request, id):
        entity=self.get_object(id)
        serializer=EntitySerializer(entity,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def delete(self,request,id):
        entity=self.get_object(id)
        entity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)