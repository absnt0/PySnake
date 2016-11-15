from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ColorScheme, HighScore
from .serializers import ColorSchemeSerializer, HighScoreSerializer

# Create your views here.

class ColorSchemeList(APIView):

    def get(self, request):
        color_schemes = ColorScheme.objects.all()
        serializer = ColorSchemeSerializer(color_schemes, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class HighScoresList(APIView):

    def get(self, request):
        high_scores = HighScore.objects.all()
        high_scores = high_scores.order_by("-score")[:10]
        serializer = HighScoreSerializer(high_scores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HighScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

