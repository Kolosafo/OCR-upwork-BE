from rest_framework import serializers
from . models import UploadImage


class UploadImageSerializer(serializers.ImageField):
    class Meta:
        model = UploadImage
        fields = ('image')
