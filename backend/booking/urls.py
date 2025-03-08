# booking/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, SlotViewSet

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'slots', SlotViewSet)

urlpatterns = [
    path('', include(router.urls)),
]