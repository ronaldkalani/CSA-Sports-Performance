from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .models import Workshop, Skill, Feedback, UserSkill
from .serializers import WorkshopSerializer, SkillSerializer, FeedbackSerializer, UserSkillSerializer
from .views import WorkshopViewSet, SkillViewSet, FeedbackViewSet, UserSkillViewSet

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class UserSkillViewSet(viewsets.ModelViewSet):
    queryset = UserSkill.objects.all()
    serializer_class = UserSkillSerializer
    permission_classes = [IsAuthenticated]

    # Filter skills by the authenticated user
    def get_queryset(self):
        return UserSkill.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user for the created UserSkill
        serializer.save(user=self.request.user)

router = DefaultRouter()
router.register(r'workshops', WorkshopViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'user-skills', UserSkillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
