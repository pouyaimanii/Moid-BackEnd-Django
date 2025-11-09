from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MovieModel
from .serializers import MovieSerializer



class MovieListView(APIView):
    def get(self, request):
        try:
            movies = MovieModel.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
