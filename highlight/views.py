from django.shortcuts import render
from .models import Highlight

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
    HighlightSerializer
)

class HighlightsView(APIView):
    def post(self, request):
        serializer = HighlightSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data = serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
