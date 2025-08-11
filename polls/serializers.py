from rest_framework import serializers
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']
        read_only_fields = ['question']
        
class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    class Meta:
        model = Question
        fields = '__all__'
        extra_fields = ['choices']
        
    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice in choices_data:
            Choice.objects.create(question=question, **choice)
        return question
    
class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_text']
    
    def update(self, question, validated_data):
        question.question_text = validated_data.get('question_text', question.question_text)
        question.save()
        return question