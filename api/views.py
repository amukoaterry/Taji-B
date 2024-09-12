from django.shortcuts import render
from rest_framework.views import APIView
from scanevent.models import ScanEvent
from .serializers import ScanEventSerializer
from rest_framework.response import Response
from rest_framework import status

class ScanEventListView(APIView):
    def get(self, request):
        scan_events = ScanEvent.objects.all()
        serializer = ScanEventSerializer(scan_events, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = ScanEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ScanEventDetailView(APIView):
    def get(self, request, id):
        scan_event = ScanEvent.objects.get(id=id)
        serializer = ScanEventSerializer(scan_event)
        return Response(serializer.data)
    def put(self, request, id):
        scan_event = ScanEvent.objects.get(id=id)
        serializer = ScanEventSerializer(scan_event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        scan_event = ScanEvent.objects.get(id=id)
        scan_event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)