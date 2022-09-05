from rest_framework import serializers
from logistic.models import Product, StockProduct, Stock


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class ProductSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'positions']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    # настройте сериализатор для склада

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')
        # address = validated_data.pop('address')

        # создаем склад по его параметрам
        stock = super().create(validated_data)
        for i in positions:
            StockProduct.objects.update_or_create(stock=stock, **i)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        for i in positions:
            StockProduct.objects.update_or_create(stock=stock, product=i['product'], price=i['price'], quantity=i['quantity'])
        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        return stock
