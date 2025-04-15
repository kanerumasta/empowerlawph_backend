from django.shortcuts import render
from rest_framework.views import APIView
from case.models import Case
from .serializers import CaseSerializer
from rest_framework import status
from rest_framework.response import Response

class CaseDetail(APIView):
    def get(self, request, id=None):
        if id:
            case = Case.objects.filter(id = id).first()
            serializer = CaseSerializer(case)
            return Response(serializer.data,status=status.HTTP_200_OK)
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
