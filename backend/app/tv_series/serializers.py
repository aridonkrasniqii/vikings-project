from rest_framework import serializers
from tv_series.models import Viking, Norseman, NFLPlayer, NflPlayerStats

from tv_series.models import VikingBase

class VikingBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = VikingBase
        fields = '__all__'

class VikingSerializer(VikingBaseSerializer):
    actor_name = serializers.CharField(max_length=255)

    class Meta(VikingBaseSerializer.Meta):
        model = Viking
        fields = '__all__'

class NorsemenSerializer(VikingBaseSerializer):
    actor_name = serializers.CharField(max_length=255)

    class Meta(VikingBaseSerializer.Meta):
        model = Norseman
        fields = '__all__'

class NFLPlayerSerializer(VikingBaseSerializer):
    position = serializers.CharField(max_length=100)
    stats = serializers.PrimaryKeyRelatedField(queryset=NflPlayerStats.objects.all(), required=False)

    class Meta(VikingBaseSerializer.Meta):
        model = NFLPlayer
        fields = '__all__'
