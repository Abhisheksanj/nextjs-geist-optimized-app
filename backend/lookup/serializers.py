from rest_framework import serializers
from .models import PhoneDirectoryEntry, SimCardData, LeakedIdentityData

class PhoneDirectoryEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneDirectoryEntry
        fields = ['number', 'name', 'region']

class SimCardDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimCardData
        fields = ['number', 'provider', 'location', 'carrier_type']

class LeakedIdentityDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeakedIdentityData
        fields = ['name', 'phone', 'address']
