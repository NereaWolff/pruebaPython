from django.db.models import fields
from rest_framework import serializers
from api.models import Patente


class PatenteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patente  
        fields = ['id','pat']