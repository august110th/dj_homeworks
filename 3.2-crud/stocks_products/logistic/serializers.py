from rest_framework import serializers
from logistic.models import Product, StockProduct, Stock


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'stocks']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for i in positions:
            StockProduct.objects.update_or_create(stock=stock, **i)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for i in positions:
            StockProduct.objects.update_or_create(stock=stock, product=i['product'], defaults={'price': i['price'], 'quantity' : i['quantity']})
        return stock
