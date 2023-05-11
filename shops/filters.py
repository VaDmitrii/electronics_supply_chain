from django_filters import rest_framework

from shops.models import FactoryStore


class CountryFilter(rest_framework.FilterSet):
    class Meta:
        model = FactoryStore
        fields = ("country",)
