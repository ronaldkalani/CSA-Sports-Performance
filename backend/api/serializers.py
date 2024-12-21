from rest_framework import serializers
from .models import Workshop, Skill, Feedback, UserSkill

class WorkshopSerializer(serializers.ModelSerializer):
    feedbacks = serializers.StringRelatedField(many=True, read_only=True)
    skills = serializers.StringRelatedField(many=True, read_only=True)  # Add related skills to the workshop

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

class UserSkillSerializer(serializers.ModelSerializer):
    skill_name = serializers.ReadOnlyField(source='skill.name')  # Include skill name in the response
    user_name = serializers.ReadOnlyField(source='user.username')  # Include username in the response

    class Meta:
        model = UserSkill
        fields = ['id', 'user', 'skill', 'skill_name', 'user_name', 'progress', 'completed']
