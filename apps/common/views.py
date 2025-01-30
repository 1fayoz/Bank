from rest_framework import generics

from apps.common import models, serializers


class CreateBlankView(generics.CreateAPIView):
    queryset = models.Blank.objects.all()
    serializer_class = serializers.CreateBlankSerializer
