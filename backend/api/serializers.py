from rest_framework import serializers
from .models import Workshop, Skill, Feedback

class WorkshopSerializer(serializers.ModelSerializer):
    feedbacks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Workshop
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
