from rest_framework import generics
from rest_framework.response import Response
from .models import ShortURL
from .serializers import ShortURLSerializer

class CreateShortURL(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

class RetrieveShortURL(generics.RetrieveAPIView):
    lookup_field = 'shortCode'
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.accessCount += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
class UpdateShortURL(generics.UpdateAPIView):
    lookup_field = 'shortCode'
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

class DeleteShortURL(generics.DestroyAPIView):
    lookup_field = 'shortCode'
    queryset = ShortURL.objects.all()

class GetStatsView(generics.RetrieveAPIView):
    lookup_field = 'shortCode'
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer