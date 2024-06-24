from rest_framework import serializers

from mpesa.models import *


class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = ("id",)
