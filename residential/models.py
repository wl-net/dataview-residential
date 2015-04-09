from django.db import models
from dataview.common.models import UUIDModel

class Residence(UUIDModel):
    name = models.CharField(max_length=64)
    location = models.ForeignKey('building.Building')
    unit_number = models.CharField(max_length=8)
    floor = models.IntegerField(default=1)
    rent = models.FloatField(default=0)
    tenants = models.ManyToManyField('auth.User', blank=True)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Neighbor(UUIDModel):
    user = models.ForeignKey('auth.User', editable=False)

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    #location = models.ForeignKey('building.Building')

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + " " + self.last_name