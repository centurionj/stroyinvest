from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from customers.models import  Question
from customers.serializer import QuestionSerializer
from customers.tasks import send_question_task


class QuestionCreateView(APIView):
    """Отправка запросов на обратную связь."""

    permission_classes = [AllowAny]

    def get_queryset(self):
        return Question.objects.all()

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)

        if serializer.is_valid():
            question_instance = serializer.save()
            send_question_task.delay(question_instance.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
