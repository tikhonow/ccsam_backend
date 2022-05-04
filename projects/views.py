from rest_framework import viewsets
from .models import Project
from .serializers import ProjectsSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = Project.objects.all()
