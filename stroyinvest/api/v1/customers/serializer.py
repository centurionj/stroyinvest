from rest_framework import serializers

from customers.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Сериалайзер заявок клиентов"""
    class Meta:
        model = Question
        fields = ('__all__')
