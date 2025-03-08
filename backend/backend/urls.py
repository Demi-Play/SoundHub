"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, UserProfileViewSet
from socialNetwork.views import MusicianProfileViewSet, GroupProfileViewSet, EventViewSet
from studio.views import EquipmentViewSet, ProjectViewSet, PortfolioItemViewSet
from booking.views import BookingViewSet, BookingSlotViewSet
from collaboration.views import ProjectFileViewSet, CollaborationRequestViewSet
from payment.views import PaymentMethodViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', UserProfileViewSet)
router.register(r'musicians', MusicianProfileViewSet)
router.register(r'groups', GroupProfileViewSet)
router.register(r'events', EventViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'portfolio', PortfolioItemViewSet)
router.register(r'slots', BookingSlotViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'files', ProjectFileViewSet)
router.register(r'requests', CollaborationRequestViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]