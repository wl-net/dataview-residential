from django.contrib import admin
from residential.models import Residence, Neighbor

class ResidenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    pass

admin.site.register(Residence, ResidenceAdmin)

class NeighborAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'location')
    pass

admin.site.register(Neighbor, NeighborAdmin)
