from rest_framework import generics
from rest_framework.response import Response
from .models import ShortURL
from .serializers import ShortURLSerializer

# create api
class CreateShortURL(generics.CreateAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

# get api
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
    
# update api
class UpdateShortURL(generics.UpdateAPIView):
    lookup_field = 'shortCode'
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

# delete api
class DeleteShortURL(generics.DestroyAPIView):
    lookup_field = 'shortCode'
    queryset = ShortURL.objects.all()

# see access frequency api
class GetStatsView(generics.RetrieveAPIView):
    lookup_field = 'shortCode'
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer