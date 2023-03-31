from rest_framework import generics
from .models import *
from .serializers import *
from .decorators import *


class productlist(generics.ListCreateAPIView):
    serializer_class = productserializer

    def get_queryset(self):
        queryset = product.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(productlocation=location)
        return queryset
               
class productdetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = productserializer
    queryset = product.objects.all()

class locationlist(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = locationserializer
    queryset = Location.objects.all()

class locationdetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = locationserializer
    queryset = Location.objects.all()
