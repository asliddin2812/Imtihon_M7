from rest_framework import serializers

from .models import Requirements
class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'
        read_only_fields = ('id',)
        