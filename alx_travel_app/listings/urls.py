from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'listings'

# Create a router for RESTful API routes
router = DefaultRouter()
router.register(r'listings', views.ListingViewSet)

urlpatterns = [
    # RESTful API URLs
    path('', include(router.urls)),
]
