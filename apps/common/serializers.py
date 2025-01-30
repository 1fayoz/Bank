from rest_framework import serializers

from apps.common import models


class CreateBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blank
        fields = (
            'latitude', 'longitude', 'photo', 'payment_amount',
            'payment_date', 'comment', 'status', 'employee'
        )
