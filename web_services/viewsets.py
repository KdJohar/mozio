import django_filters
from django.contrib.gis.geos import Point
from rest_framework import viewsets
from rest_framework.response import Response

from area_providers.models import ServiceArea, Provider
from .serializers import ProviderSerializer, ServiceAreaSerializer


class PointFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr=['exact', 'iexact'])


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def list(self, request):
        lattitude = request.query_params.get('lattitude', None)
        longitude = request.query_params.get('longitude', None)
        query_dict = {}
        if lattitude and longitude:
            try:
                point = Point(float(lattitude), float(longitude))
                query_dict = {'polygon__intersects': point}
            except:
                pass
        queryset = ServiceArea.objects.filter(**query_dict)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ServiceAreaSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ServiceAreaSerializer(queryset, many=True)
        return Response(serializer.data)


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
