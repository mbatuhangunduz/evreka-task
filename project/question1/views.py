from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import *
from .models import *
from .serializers import *
from django.utils import timezone
from datetime import timedelta


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    http_method_names = ['get', 'post'] # This line is used to allow which http methods are allowed to be used. Also all of the viewset that are created will have the same http methods.


class NavigationRecordViewSet(viewsets.ModelViewSet):
    queryset = NavigationRecord.objects.all()
    serializer_class = NavigationRecordSerializer
    http_method_names = ['get', 'post']  

    """
    Both functions below get exactly the same response. I used the pagination structure for both functions. Performance can be increased by sending limit and offset
    parameters that come from pagination. In addition, if much larger data is used, elastic search can be best option to get a faster response and filter.
    """

    def list(self, request, *args, **kwargs):
        vehicle_plate = request.GET.get('vehicle_plate') # This line is used to allow the user to send the vehicle_plate as a query parameter.
        request_time = timezone.localtime() - timedelta(hours=48)

        """If it is sent as a query parameter, it only returns the 48-hour data of that plate."""
        if vehicle_plate:
            """The following 2 lines were written to eliminate the problems that may occur when sending parameters, such as small-capital letters or leaving spaces."""
            vehicle_plate = vehicle_plate.replace(" ", "")
            vehicle_plate = vehicle_plate.upper()
            last_points = NavigationRecord.objects.filter(vehicle__plate=vehicle_plate, datetime__gte=request_time).order_by('-datetime')
            serializer = NavigationRecordListSerializer(last_points, many=True).data
            return Response(serializer, status=status.HTTP_200_OK)
            """
              (If pagination will  be used, 
            following two lines [51, 52] should be uncomment and comment out the 46th line. This also applies to below function.)
            """
            # page = self.paginate_queryset(serializer)
            # return self.get_paginated_response(page)
            
        last_points = NavigationRecord.objects.filter(datetime__gte=request_time).order_by('-datetime')
        serializer = NavigationRecordListSerializer(last_points, many=True).data
        return Response({"last_points":serializer}, status=status.HTTP_200_OK)
        # page = self.paginate_queryset(serializer)
        # return self.get_paginated_response({"last_points":serializer})

    
    @action(detail=False, methods=['get'])
    def last_points(self, request, *args, **kwargs):
        vehicle_plate = request.GET.get('vehicle_plate')
        request_time = timezone.localtime() - timedelta(hours=48)

        """If it is sent as a query parameter, it only returns the 48-hour data of that plate."""
        if vehicle_plate:
            """The following 2 lines were written to eliminate the problems that may occur when sending parameters, such as small-capital letters or leaving spaces."""
            vehicle_plate = vehicle_plate.replace(" ", "")
            vehicle_plate = vehicle_plate.upper()
            records = NavigationRecord.objects.filter(vehicle__plate=vehicle_plate).order_by('-datetime')
            last_points = []
            for record in records:
                if record.datetime >= request_time:
                    last_points.append(record)
            serializer = NavigationRecordListSerializer(last_points, many=True).data
            return Response(serializer, status=status.HTTP_200_OK)
            # page = self.paginate_queryset(serializer)
            # return self.get_paginated_response(page)

        records = NavigationRecord.objects.all().order_by('-datetime')
        last_points = []

        for record in records:
            if record.datetime >= request_time:
                last_points.append(record)
        serializer = NavigationRecordListSerializer(last_points, many=True).data
        return Response({"last_points":serializer}, status=status.HTTP_200_OK)
        # page = self.paginate_queryset(serializer)
        # return self.get_paginated_response(page)
