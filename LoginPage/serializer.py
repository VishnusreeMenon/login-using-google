from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email','first_name','last_name','username']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Profile
        fields = ['role','company','intrest','user']
        extra_kwargs = {
           "user": {'read_only': True},
        }
        
    def create(self, validated_data):   #for nested fields
       
        data = validated_data.pop('user')
        user = get_user_model().objects.create_user(**data)
        validated_data.update({'user': user})
        profile,created = Profile.objects.update_or_create(user = validated_data.get('user'),defaults={'role':validated_data.get('role'),'company':validated_data.get('company'),'intrest':validated_data.get('intrest')} )
        
        
        return profile
    # create(user)