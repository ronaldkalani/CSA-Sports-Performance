from rest_framework.routers import DefaultRouter
from .views import WorkshopViewSet, SkillViewSet, FeedbackViewSet

# Initialize the DefaultRouter
router = DefaultRouter()

# Register the viewsets
router.register(r'workshops', WorkshopViewSet)  # Handles /api/workshops/
router.register(r'skills', SkillViewSet)        # Handles /api/skills/
router.register(r'feedbacks', FeedbackViewSet)  # Handles /api/feedbacks/

# Assign router.urls to urlpatterns
urlpatterns = router.urls

