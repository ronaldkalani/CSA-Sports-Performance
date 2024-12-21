from django.db import models
from django.contrib.auth.models import User

class Workshop(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    duration = models.IntegerField(help_text="Duration in hours")
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Feedback(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='feedbacks')
    attendee_name = models.CharField(max_length=255)
    comments = models.TextField()
    rating = models.PositiveSmallIntegerField()  # Rating out of 5

    def __str__(self):
        return f"{self.attendee_name} - {self.workshop.name}"

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='user_skills')
    progress = models.IntegerField(default=0, help_text="Progress in percentage")
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'skill')  # Prevent duplicate entries for the same user and skill

    def __str__(self):
        return f"{self.user.username} - {self.skill.name}"
