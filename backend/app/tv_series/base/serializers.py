
from tv_series.base.models.base_models import VikingBase
from tv_series.nfl_players.nfl_players_model import NFLPlayer, NflPlayerStats
from tv_series.norsemans.norsemen_models import Norseman
from tv_series.vikings.vikings_model import Viking

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
    season = serializers.IntegerField()  # Season year
    team = serializers.CharField(max_length=255)  # Team for the season
    games_played = serializers.IntegerField(default=0)  # Total games played
    receptions = serializers.IntegerField(default=0)  # Total receptions
    receiving_yards = serializers.IntegerField(default=0)  # Total receiving yards
    receiving_touchdowns = serializers.IntegerField(default=0)  # Receiving touchdowns
    longest_reception = serializers.IntegerField(default=0)  # Longest reception in yards

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

