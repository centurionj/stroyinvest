from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from api.v1.customers.serializer import QuestionSerializer
from customers.tasks import send_question_task
from customers.models import Question


class QuestionViewSet(ModelViewSet):
    """Вью-сет заявки (вопроса на сайте)."""

    permission_classes = [AllowAny]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            question_instance = serializer.save()
            send_question_task.delay(question_instance.id)
            return Response(data={'id': serializer.data.get('id')}, status=status.HTTP_201_CREATED)

        return Response(data={'id': serializer.data.get('id')}, status=status.HTTP_400_BAD_REQUEST)
