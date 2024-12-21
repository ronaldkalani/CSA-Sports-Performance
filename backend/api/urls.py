from rest_framework.routers import DefaultRouter
from .views import WorkshopViewSet, SkillViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'workshops', WorkshopViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = router.urls

