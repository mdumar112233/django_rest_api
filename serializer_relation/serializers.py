from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song_detail')
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # song = serializers.HyperlinkedIdentityField(many=True, read_only=True, view_name='song-detail')

    #### NESTED SERIALIZER
    songby = SongSerializer(many=True, read_only=True)
    
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songby']





