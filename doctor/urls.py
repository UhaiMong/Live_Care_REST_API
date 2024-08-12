from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'list', views.DoctorViewSet)
router.register(r'designation', views.DesignationViewSet)
router.register(r'specialization', views.SpecializationViewSet)
router.register(r'available_time', views.AvailableTimeViewSet)
router.register(r'review', views.ReviewViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]