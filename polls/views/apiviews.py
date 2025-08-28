from rest_framework.views import APIView
from rest_framework.response import Response
from polls.serializers import QuestionSerializer, QuestionUpdateSerializer
from polls.models import Question
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse

class CustomSerialization(APIView):
    def get(self, request):
        questions = Question.objects.all()
        data = []
        for question in questions:
            data.append({
                "id": question.id,
                "question_text": question.question_text,
            })
        return JsonResponse(data, safe=False)

class QuestionsView(APIView):
    
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def patch(self, request, pk):
        question = Question.objects.get(pk=pk)
        serializer = QuestionUpdateSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            question = Question.objects.get(pk=pk)
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
class TestSecurityView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        return Response({"message": "Hello, secured world! The request was permitted."})
