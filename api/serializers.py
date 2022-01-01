from django.db.models import fields
from rest_framework import serializers
from .models import Voterdb

class VoterdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voterdb
        fields = '__all__'