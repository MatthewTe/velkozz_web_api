# Importing serializer methods:
from rest_framework import serializers

# Importing the Market Index Data Models:
from .market_indicies_models import *

# Abstract class for Indicies:
class MarketIndexSerializers(serializers.HyperlinkedModelSerializer):

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(MarketIndexSerializers, self).__init__(many=many, *args, **kwargs)

    class Meta:
        fields = "__all__"

# Creating the Market Index Serializers from the Abstract class:
class SPYIndexSerializer(MarketIndexSerializers):    
    class Meta(MarketIndexSerializers.Meta):
        model = SPYIndexComposition

class DJIAIndexSerializer(MarketIndexSerializers):
    class Meta(MarketIndexSerializers.Meta):
        model = DJIAIndexComposition
    
class SPTSXIndexSerializer(MarketIndexSerializers):
    class Meta(MarketIndexSerializers):
        model = SPTSXIndexComposition

class FTSE100IndexSerializer(MarketIndexSerializers):
    class Meta(MarketIndexSerializers):
        model = FTSE100IndexComposition

class SMISerializer(MarketIndexSerializers):
    class Meta(MarketIndexSerializers):
        model = SMIComposition

class SPISerializer(MarketIndexSerializers):
    class Meta(MarketIndexSerializers):
        model = SPIComposition
