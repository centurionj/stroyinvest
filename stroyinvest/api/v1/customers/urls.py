from rest_framework.routers import DefaultRouter

from api.v1.customers.views import QuestionViewSet

router = DefaultRouter()
router.register('question_create', QuestionViewSet, basename='question_create')

urlpatterns = []

urlpatterns += router.urls
