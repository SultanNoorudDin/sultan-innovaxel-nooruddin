from rest_framework import status, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import ShortURL
from .serializers import ShortURLSerializer

class CreateShortURL(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer
