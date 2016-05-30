
from residential.api.serializers import ResidenceSerializer, PackageSerializer
from residential.models import *

from rest_framework import viewsets, filters
import django_filters


class ResidenceViewSet(viewsets.ModelViewSet):
    queryset = Residence.objects.all()
    serializer_class = ResidenceSerializer


class ResidenceFilter(django_filters.FilterSet):
    class Meta:
        model = Residence
        fields = ('name', 'unit_number', 'floor')

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class PackageFilter(django_filters.FilterSet):
    class Meta:
        model = Package
        fields = ('time', 'residence', 'perishable')