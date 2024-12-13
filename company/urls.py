from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, WorkerViewSet, AttendanceViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'workers', WorkerViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]