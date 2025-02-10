from api.base.models.base_models import VikingBase
from api.nfl_players.nfl_players_model import NFLPlayer, NflPlayerStats
from api.norsemans.norsemen_models import Norseman
from api.vikings.vikings_model import Viking

from rest_framework import serializers

class VikingBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = VikingBase
        fields = '__all__'

class VikingSerializer(VikingBaseSerializer):
    actor_name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000)

    class Meta(VikingBaseSerializer.Meta):
        model = Viking
        fields = '__all__'

class NorsemanSerializer(VikingBaseSerializer):
    actor_name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=1000)

    class Meta(VikingBaseSerializer.Meta):
        model = Norseman
        fields = '__all__'

class NFLPlayerStatsSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(queryset=NFLPlayer.objects.all())
    season = serializers.IntegerField()
    team = serializers.CharField(max_length=255)
    games_played = serializers.IntegerField(default=0)
    receptions = serializers.IntegerField(default=0)
    receiving_yards = serializers.IntegerField(default=0)
    receiving_touchdowns = serializers.IntegerField(default=0)
    longest_reception = serializers.IntegerField(default=0)

    class Meta:
        model = NflPlayerStats
        fields = '__all__'


class NFLPlayerSerializer(serializers.ModelSerializer):
    stats = NFLPlayerStatsSerializer(many=True, read_only=True)
    number = serializers.IntegerField(required=False)
    position = serializers.CharField(max_length=100, required=False)
    age = serializers.IntegerField(required=False)
    experience = serializers.IntegerField(required=False)
    college = serializers.CharField(max_length=255, required=False)

    class Meta:
        model = NFLPlayer
        fields = '__all__'


class PaginatedVikingSerializer(serializers.Serializer):
    total_items = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    current_page = serializers.IntegerField()
    limit = serializers.IntegerField()
    data = VikingSerializer(many=True)

class PaginatedNorsemanSerializer(serializers.Serializer):
    total_items = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    current_page = serializers.IntegerField()
    limit = serializers.IntegerField()
    data = NorsemanSerializer(many=True)

class PaginatedNFLPlayerSerializer(serializers.Serializer):
    total_items = serializers.IntegerField()
    total_pages = serializers.IntegerField()
    current_page = serializers.IntegerField()
    limit = serializers.IntegerField()
    data = NFLPlayerSerializer(many=True)

