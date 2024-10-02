from rest_framework import serializers

from website.models import Cart, Product


class ProductSerializer(serializers.ModelSerializer):
    custom_name = serializers.SerializerMethodField(
        method_name="get_custom_name"
    )
    owners = serializers.SerializerMethodField(
        method_name="get_owners"
    )

    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "custom_name",
            "owners",
            "created",
            "updated",
        ]

    def get_custom_name(self, obj: Product):
        return f"custom_{obj.name}"

    def get_owners(self, obj: Product):
        carts = Cart.objects.filter(products=obj)
        cart_ids = [cart.id for cart in carts] # type: ignore
        
        return cart_ids