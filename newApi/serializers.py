from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    namel= serializers.SerializerMethodField()
    class Meta:
        model = User  # Specify the model that the serializer is associated with
        fields = '__all__'
        

    def validate_name(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Invalid name")
        else:
            return value.title()
    

    def get_namel(self,object):
     name= len(object.name)
     return name
    


    


     def validate(self, data):
        
        if data['name'] != data['name'].lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return data['name']












    # def validate(self, data):
       
    #     if data['name'] ==data['address']:
    #         raise serializers.ValidationError("finish must occur after start")
    #     return data