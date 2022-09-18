from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement
from django_filters.widgets import RangeWidget


class AdvertisementFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator']
