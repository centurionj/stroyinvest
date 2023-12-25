from django.core.mail import send_mail
from django.conf import settings

from celery import shared_task

from customers.models import Question

@shared_task
def send_question_task(question_id):
    """
    Отправка сообщения о заданном вопросе на сайте.
    """
    question_instance = Question.objects.get(pk=question_id)

    user_subject = 'Обратная связь'
    user_message = (
        f'{question_instance.message}\n\n'
        f'Имя отправителя: {question_instance.name}\n'
        f'Телефон отправителя: {question_instance.phone}\n'
        f'Почта отправителя: {question_instance.email}'
    )

    send_mail(
        user_subject,
        user_message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_RECEIVER]
    )
