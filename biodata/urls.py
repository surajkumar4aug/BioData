from django.urls import include, path
from rest_framework import routers
from .views import MarriageBiodataViewSet, html_file_view, MarriageBiodataAPIView

router = routers.DefaultRouter()
router.register(r'marriage-biodata', MarriageBiodataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('html-file/', html_file_view, name='html_file'),
    path('marriage/', MarriageBiodataAPIView.as_view(), name='html_file'),
]
