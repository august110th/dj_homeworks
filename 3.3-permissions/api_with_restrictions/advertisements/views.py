from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from advertisements.models import Advertisement
from .serializers import AdvertisementSerializer
from .permissions import IsOwner
from .filters import AdvertisementFilter


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AdvertisementFilter
    search_fields = ['title', 'description', 'creator', 'created_at']

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "delete", "update", "partial_update"]:
            return [IsAuthenticated(), IsOwner()]
        return []
