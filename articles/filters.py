from django_filters.rest_framework import FilterSet
from .models import Space, Property

class SpaceFilter(FilterSet):
    class Meta:
        model = Space
        fields = {
            'address': ['exact'],
            'city': ['exact'],
            'type': ['exact'],
            'price': ['gt', 'lt']
        }


class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'category': ['exact'],
            'city': ['exact'],
            'address': ['exact'],
            'price': ['gt', 'lt']
        }