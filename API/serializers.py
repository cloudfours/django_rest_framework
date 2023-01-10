from rest_framework import serializers
from .models import *

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','title','description','technology','created_add')
        read_only=('created_add',)

