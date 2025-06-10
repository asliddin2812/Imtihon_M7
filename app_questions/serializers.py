from rest_framework import serializers
from .models import AskedQuestions

class AskedQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AskedQuestions
        fields = ['id', 'question', 'answer']
