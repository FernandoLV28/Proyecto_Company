from rest_framework import viewsets
from django.http import HttpResponse
from .models import Company, Worker, Attendance
from .serializers import CompanySerializer, WorkerSerializer, AttendanceSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

def home_view(request):
    return HttpResponse("<h1>Bienvenido a la API de Company</h1><p>Utiliza las siguientes rutas:</p><ul><li>/api/companies/</li><li>/api/workers/</li><li>/api/attendance/</li></ul>")
