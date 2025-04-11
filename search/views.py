from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, SearchHeadline
from django.db.models.expressions import RawSQL
from django.db import connection

from case.models import Case
from case.serializers import CaseSerializer

class SearchView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "q", openapi.IN_QUERY, 
                description="Search keyword", 
                type=openapi.TYPE_STRING,
                required=False
            )
        ],
        responses={200: "List of matching cases and statutes"}
    )
    def get(self, request):
        query = self.request.GET.get('q','')
        search_vector = SearchVector("title","full_text")
        search_query = SearchQuery(query)
        search_headline = SearchHeadline("full_text", search_query)
        
        cases_results = Case.objects.annotate(rank=SearchRank(search_vector, search_query)).annotate(headline = search_headline).filter(rank__gte = 0.001)

        for result in cases_results:
            print(result.headline)
        case_serializer = CaseSerializer(cases_results, many=True)

        return Response({"cases":case_serializer.data}, status=status.HTTP_200_OK)

        