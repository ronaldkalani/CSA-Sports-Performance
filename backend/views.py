from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
import json

# In-memory data store (replace with a database for production)
workshops = []
skills = []
feedback = []

# ---------------------
# Workshops Endpoints
# ---------------------
def get_workshops(request):
    """Retrieve all workshops."""
    return JsonResponse({'workshops': workshops}, safe=False)

@csrf_exempt
def add_workshop(request):
    """Add a new workshop."""
    if request.method == 'POST':
        data = json.loads(request.body)
        if not data or 'title' not in data or 'date' not in data:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        workshop = {
            'id': len(workshops) + 1,
            'title': data['title'],
            'description': data.get('description', ''),
            'date': data['date']
        }
        workshops.append(workshop)
        return JsonResponse({'message': 'Workshop added successfully', 'workshop': workshop}, status=201)

# ---------------------
# Skills Endpoints
# ---------------------
def get_skills(request):
    """Retrieve all tracked skills."""
    return JsonResponse({'skills': skills}, safe=False)

@csrf_exempt
def add_skill(request):
    """Track a new skill."""
    if request.method == 'POST':
        data = json.loads(request.body)
        if not data or 'name' not in data or 'description' not in data:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        skill = {
            'id': len(skills) + 1,
            'name': data['name'],
            'description': data['description'],
            'athletes': data.get('athletes', [])
        }
        skills.append(skill)
        return JsonResponse({'message': 'Skill added successfully', 'skill': skill}, status=201)

# ---------------------
# Feedback Endpoints
# ---------------------
def get_feedback(request):
    """Retrieve all feedback."""
    return JsonResponse({'feedback': feedback}, safe=False)

@csrf_exempt
def add_feedback(request):
    """Submit feedback."""
    if request.method == 'POST':
        data = json.loads(request.body)
        if not data or 'athlete_id' not in data or 'comments' not in data:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        feedback_entry = {
            'id': len(feedback) + 1,
            'athlete_id': data['athlete_id'],
            'comments': data['comments'],
            'rating': data.get('rating', 0)
        }
        feedback.append(feedback_entry)
        return JsonResponse({'message': 'Feedback submitted successfully', 'feedback': feedback_entry}, status=201)

# ---------------------
# Health Check
# ---------------------
def health_check(request):
    """Health check endpoint to verify the server is running."""
    return JsonResponse({'status': 'ok'}, status=200)

# ---------------------
# URL Configuration
# ---------------------
urlpatterns = [
    path('api/workshops', get_workshops),
    path('api/workshops', add_workshop),
    path('api/skills', get_skills),
    path('api/skills', add_skill),
    path('api/feedback', get_feedback),
    path('api/feedback', add_feedback),
    path('api/health', health_check),
]
