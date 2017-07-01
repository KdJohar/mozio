from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from area_providers.models import ServiceArea, Provider


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    """ A class to serialize locations as GeoJSON compatible data """

    class Meta:
        model = ServiceArea
        geo_field = "polygon"
        fields = '__all__'
        depth = 1


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
