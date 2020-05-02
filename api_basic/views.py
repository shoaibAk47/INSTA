from .models import Entity
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.contrib.auth.models import User  
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