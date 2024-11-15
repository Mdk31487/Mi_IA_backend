from django.shortcuts import render

# Create your views here.
nano interacciones/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Interaccion
from .serializers import InteraccionSerializer

class InteraccionView(APIView):
    def post(self, request):
        serializer = InteraccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("¡Bienvenido a la IA!")
