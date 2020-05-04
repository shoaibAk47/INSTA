from .models import Entity
from .serializers import RegisterSerializer, EntitySerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthenticatedAndOwner
from django.http import Http404

# Create your views here.
def home(request):
    return HttpResponse('Welcome to Insta')
@api_view(['POST'])
def RegisterView(request):
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ShowUser(request):
    user=User.objects.all()
    serializer=RegisterSerializer(user,many=True)
    return Response(serializer.data)


class EntityAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        entities=Entity.objects.filter(user=request.user)
        serializer=EntitySerializer(entities,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=EntitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class EntityDetails(APIView):
    permission_classes=[IsAuthenticated, IsAuthenticatedAndOwner]
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
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        entity=self.get_object(id)
        entity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)