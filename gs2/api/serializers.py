from rest_framework  import serializers
from .models import Student


#validators reusable
def stat_with_r(value):
	if value[0].lower() != 'r':
		raise serializers.ValidationError("name should start with r")
	return value

class StudentSerializer(serializers.Serializer):
    # id=serializers.IntegerField()
    name=serializers.CharField(max_length=100,validators=[stat_with_r])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)


    def create(self, validated_data):
        return Student.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance

#Field level validations:
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('seats full!!')
        return value


#Object level validation:
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == "rohit" and ct.lower() != 'ddn':
            raise serializers.ValidationError('City must be DDN for rohit!!')
        return data
        