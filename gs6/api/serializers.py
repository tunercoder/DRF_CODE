from rest_framework  import serializers
from rest_framework.fields import ReadOnlyField
from .models import Student




class StudentSerializer(serializers.ModelSerializer):
    #validators reusable
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError("name should start with r")
        return value
        
    #validation for specific single field name can be added like this in ModelSerializer
    # name=serializers.CharField(read_only=True)
    name=serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields=['name','roll'] #to allow multiple field validations on ModelSerializer in single line
        # extra_kwargs={'name':{'read_only':True}} #validation properties using extra_kwargs attribute in ModelSerializers


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
        