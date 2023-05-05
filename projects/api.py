from .models import Projects
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    #allow permite revision de cualquier cliente 
    permission_classes = [permissions.AllowAny]
    #aplicando el serializer
    serializer_class = ProjectSerializer