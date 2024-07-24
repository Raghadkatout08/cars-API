from rest_framework import serializers 
from .models import Car

class CarSerializers(serializers.ModelSerializer):

    buy_time = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['buyer_id', 'model', 'brand', 'price', 'is_bought', 'buy_time']

    def get_buy_time(self, obj):
        return obj.buy_time.date() if obj.buy_time else None