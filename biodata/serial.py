from rest_framework import serializers
from .models import MarriageBiodata

class MarriageBiodataSerializer(serializers.ModelSerializer):
    education_3 =serializers.CharField(required=False)
    education_4 =serializers.CharField(required=False)
    weight =serializers.CharField(required=False)
    class Meta:
        model = MarriageBiodata
        #fields = [' name','dob','gender','marital_status',]
        fields = '__all__'
        
        
