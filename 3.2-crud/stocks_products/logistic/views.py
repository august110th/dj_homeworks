from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'description']
    search_fields = ['title', 'description']
    # при необходимости добавьте параметры фильтрации


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['products']
    search_fields = ['products']
    # при необходимости добавьте параметрпараметрыы фильтрации


class StockInfoView(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def post(self, request, **kwargs):
        return Response(Stock.objects.all())


class ProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, **kwargs):
        return Response(Product.objects.all())


class StockView(RetrieveUpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class StockCreate(CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDataView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StockDelete(CreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)