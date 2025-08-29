from rest_framework import serializers
from .models import Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']
        read_only_fields = ['question']
        
class TestQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question_text = serializers.CharField(max_length=200)
    # pub_date = serializers.DateTimeField()
    # choices = ChoiceSerializer(many=True)

    # Método POST
    def create(self, validated_data):
        validated_data.pop('id')
        validated_data["pub_date"] = "2025-01-01 00:00:00"
        question = Question.objects.create(**validated_data)
        return question

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
        fields = '__all__'
        extra_fields = ['choices']
    
    def update(self, question, validated_data):
        print(validated_data)
        choices_data = validated_data.pop('choices')
        question.question_text = validated_data.get('question_text', question.question_text)
        question.pub_date = validated_data.get('pub_date', question.pub_date)

        for new_choice in choices_data:
            print(new_choice)
            target_choice = Choice.objects.get(pk=new_choice.get('id'))
            target_choice.choice_text = new_choice.get('choice_text', target_choice.choice_text)
            target_choice.votes = new_choice.get('votes', target_choice.votes)
            target_choice.save()

        question.save()
        return question