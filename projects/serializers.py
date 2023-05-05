from rest_framework import serializers
from .models import Projects
#con esto se serializa los datos ya migrados
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'rute', 'users', 'keys', 'creat_at')
        read_only_fields = ('creat_at',)