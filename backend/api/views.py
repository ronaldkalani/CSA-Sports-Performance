from rest_framework import viewsets
from .models import Workshop, Skill, Feedback
from .serializers import WorkshopSerializer, SkillSerializer, FeedbackSerializer

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset = Workshop.objects.all()
    serializer_class = WorkshopSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
