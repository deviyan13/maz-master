from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.query import QuerySet
from main.models import SimplifiedPackage
from main.serializers import (
    SimplifiedPackageSerializer, 
    CarSerializer,
    CarPositionSerializer,
)

class CarsListView(generics.GenericAPIView):
    '''View for getting available cars'''
    serializer_class = CarSerializer
    queryset = SimplifiedPackage.objects.all()

    def get(self, request, *args, **kwargs):
        cars_vin = SimplifiedPackage.objects.values('vin').annotate(dcount = Count('vin'))
        print(cars_vin)

        serializer = self.serializer_class(cars_vin, many=True)
        return Response(status=200, data=serializer.data)

class CarDetailView(generics.GenericAPIView):
    '''
        View for get information about car

        [params]
        ?vin={vin} - required, vin of car
        &sort_date_from={datetime} - optional, from which date you need data about car
        &sort_date_to={datetime} - optional, to which date you need data about car
    '''
    serializer_class = CarPositionSerializer
    queryset = SimplifiedPackage.objects.all()

    def get(self, request, *args, **kwargs):
        vin = request.query_params.get('vin', default=None)
        if vin == None:
            return Response(status = 400, data={'message':"Request should contain vin of car by GET params."})
        
        sort_date_from = request.query_params.get('datetime_from', default=None)
        sort_date_to = request.query_params.get('datetime_to', default=None)
        res = SimplifiedPackage.objects.values('id','vin','datetime','latitude','longitude').filter(vin=vin).order_by('datetime')

        if sort_date_from:
            res = res.filter(datetime__gt=sort_date_from)
        
        if sort_date_to:
            res = res.filter(datetime_lt=sort_date_to)


        serializer = self.serializer_class(res, many=True)
        return Response(status=200, data=serializer.data)

class CarPostitionView(generics.GenericAPIView):
    '''
        View for getting simplified package of current car in moment

        [params]
        ?vin={vin} - required, vin of car
        &datetime={datetime} - required, datetime of moment which statistics you need
    '''
    serializer_class = SimplifiedPackageSerializer
    queryset = SimplifiedPackage.objects.all()

    def get(self, request, *args, **kwargs):
        vin = request.query_params.get('vin', default=None)
        if vin == None:
            return Response(status = 400, data={'message':"Request should contain vin of car by GET params."})

        date = request.query_params.get('datetime', default=None)
        if date == None:
            return Response(status = 400, data={'message':"Request should contain datetime of moment by GET params."})

        res = SimplifiedPackage.objects.filter(vin=vin, datetime=date)

        if len(res)==0:
            return Response(status = 404, data={'message': "No data found."})

        serializer = self.serializer_class(res[0])

        return Response(status=200, data=serializer.data)

