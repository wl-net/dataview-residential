from residential.models import Residence, Package
from rest_framework import serializers


class ResidenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Residence
        fields = ['name', 'unit_number', 'floor', ]


class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ['courier', 'time', 'residence']