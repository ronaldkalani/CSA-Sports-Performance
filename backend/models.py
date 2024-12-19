# models.py

from django.db import models

class Workshop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    athletes = models.JSONField(default=list)  # Store list of athletes

    def __str__(self):
        return self.name


class Feedback(models.Model):
    athlete_id = models.IntegerField()
    comments = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"Feedback from Athlete {self.athlete_id}"
