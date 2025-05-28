from rest_framework import serializers
from .models import Product, Order, OrderItem
from .services.translation_service import translate_text

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    short_description_translated = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id','name','image','price','stock','short_description', 'short_description_translated', 'product_description'

    def get_short_description_translated(self, obj):
        request = self.context.get('request')

        lang = getattr(request, 'LANGUAGE_CODE', 'en').upper()

        if lang == 'EN':
            return obj.short_description

        try:
            return translate_text(obj.short_description, target_lang=lang)
        except Exception:
            return obj.short_description

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'customer_name', 'customer_email', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            if product.stock >= quantity:
                product.stock -= quantity
                product.save()
            else:
                raise serializers.ValidationError(
                    f"Not enough stock for product: {product.name} (available: {product.stock})"
                )

            OrderItem.objects.create(order=order, **item_data)

        return order

