from rest_framework import serializers
from .models import MarriageBiodata

class MarriageBiodataSerializer(serializers.ModelSerializer):
    #education_3 =serializers.CharField(allow_blank=True, required=False)
    exclude=['education_3']
    class Meta:
        model = MarriageBiodata
        fields = ('education','education_2','education_3')
        
