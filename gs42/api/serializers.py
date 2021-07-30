from rest_framework  import serializers
from rest_framework.fields import ReadOnlyField
from .models import Singer,Song


class SingerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Singer
        fields = ['id','url','name','gender','song']



class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title','singer','duration']
        

