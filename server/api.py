from tastypie.resources import ModelResource, ALL
from server.models import Attraction

class AttractionResource(ModelResource):
    class Meta:
        queryset = Attraction.objects.all()
        resource_name="attraction"
        filtering = {'city':ALL}