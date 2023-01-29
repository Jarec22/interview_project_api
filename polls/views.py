from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer


class QuestionsList(APIView):

    def get(self, request, format=None):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

class ChoicesDetail(APIView):

    def get(self, request, pk, format=None):
        question = Question.objects.get(pk=pk)
        choices = question.choice_set.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)