from rest_framework import viewsets
from .serializers import *
from .models import *


class BinViewSet(viewsets.ModelViewSet):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer
    http_method_names = ['get', 'post']

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
    http_method_names = ['get', 'post']


class BinOperationViewSet(viewsets.ModelViewSet):
    queryset = BinOperation.objects.all()
    http_method_names = ['get', 'post']
    serializer_class = BinOperationSerializer


    def get_serializer_class(self):
        if self.action == 'list':
            return BinOperationListSerializer
        else: 
            return BinOperationSerializer
    