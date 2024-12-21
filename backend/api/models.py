from django.db import models

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
