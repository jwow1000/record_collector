from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Record
from .serializers import RecordSerializer

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