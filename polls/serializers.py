from rest_framework import serializers
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(
        queryset = Question.objects.all(),
        source = 'question.id',
    )
    class Meta:
        model = Choice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    children = ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = '__all__'