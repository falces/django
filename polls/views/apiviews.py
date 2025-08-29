from rest_framework.views import APIView
from rest_framework.response import Response
from polls.serializers import QuestionSerializer, QuestionUpdateSerializer, TestQuestionSerializer, TestQuestionSerializerUpdate
from polls.models import Question
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import JsonResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='post', request_body=TestQuestionSerializer)
@api_view(['GET', 'POST'])
def testSerializer(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = TestQuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)
    
    if request.method == 'POST':
        serializer = TestQuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['PUT'])
def updateQuestion(request, pk):
    try:
        question = Question.objects.get(pk=pk)
        if request.method == 'PUT':
            serializer = TestQuestionSerializerUpdate(question, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=204)
            return Response(serializer.errors, status=400)
    except Question.DoesNotExist:
        return Response("Not found", status=404)


@api_view(['GET', 'POST'])
def testMultiMethod(request):
    if request.method == 'GET':
        return JsonResponse({"message": "GET"})
    elif request.method == 'POST':
        return JsonResponse({"message": "POST"}, status=201)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)


@api_view(['GET'])
def testFuncionView(request):
    return JsonResponse({"message": "Hello, world!"})

@api_view(['GET'])
def testFuncionViewResponse(request):
    return Response(
        {"message": "Response from Response"},
        status=200,
    )

class testClassView(APIView):
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
