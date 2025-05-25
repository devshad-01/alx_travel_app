from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    """
    class Meta:
        model = Listing
        fields = '__all__'
