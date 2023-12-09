from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from customers.models import  Question
from customers.serializer import QuestionSerializer


class QuestionCreateView(APIView):
    """Отправка запросов на обратную связь."""

    permission_classes = [AllowAny]

    def get_queryset(self):
        return Question.objects.all()

    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
