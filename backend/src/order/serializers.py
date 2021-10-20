from django.db.models import Count
from rest_framework import serializers

from account.serializers import ProfileSerializer
from .models import ShipDistance, Order, ProductOrder


class ShipDistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipDistance
        fields = "__all__"


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        exclude = ("order",)


class OrderSerializer(serializers.ModelSerializer):
    consignor = serializers.SerializerMethodField()
    consignee = ProfileSerializer(read_only=True)
    products = ProductOrderSerializer(read_only=True, many=True)
    dateCreated = serializers.DateTimeField(format="%d-%m-%Y")

    def get_consignor(self, obj):
        consignorProfile = ProfileSerializer(obj.user.profile, many=False)

        return consignorProfile.data

    class Meta:
        model = Order
        exclude = ("user", )

