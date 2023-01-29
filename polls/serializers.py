from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question_text',
            'pub_date',
        )
        model = Question

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'question',
            'choice_text',
            'votes',
        )
        model = Choice