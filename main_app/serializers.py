from rest_framework import serializers
from .models import Record, Spin

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class SpinSerializer(serializers.ModelSerializer):
  class Meta:
    model = Spin
    fields = '__all__'
    read_only_fields = ('record',)