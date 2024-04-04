from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Record, Spin, Dj
from .serializers import RecordSerializer, SpinSerializer, DjSerializer

# Define the home view
class Home(APIView):
  def get(self, request):
    content = {'message': 'Welcome to the record-collector api home route!'}
    return Response(content)

class RecordList(generics.ListCreateAPIView):
  queryset = Record.objects.all()
  serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Record.objects.all()
  serializer_class = RecordSerializer
  lookup_field = 'id'

class SpinListCreate(generics.ListCreateAPIView):
  serializer_class = SpinSerializer

  def get_queryset(self):
    record_id = self.kwargs['record_id']
    return Spin.objects.filter(record_id=record_id)
  
  def perform_create(self, serializer):
    record_id = self.kwargs['record_id']
    record = Record.objects.get(id=record_id)
    serializer.save(record=record)

class SpinDetail(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = SpinSerializer
  lookup_field = 'id'

  def get_queryset(self):
    record_id = self.kwargs['record_id']
    return Spin.objects.filter(record_id=record_id)

class SpinList(generics.ListCreateAPIView):
  queryset = Spin.objects.all()
  serializer_class = SpinSerializer

# -- - - - - -  - - - class Dj
class DjList(generics.ListCreateAPIView):
  queryset = Dj.objects.all()
  serializer_class = DjSerializer

class DjDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Record.objects.all()
  serializer_class = DjSerializer
  lookup_field = 'id'

  