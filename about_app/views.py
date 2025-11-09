from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AboutModel
from .serializers import AboutSerializer



class AboutListView(APIView):
    def get(self, request):
        try:
            about = AboutModel.objects.all()
            serializer = AboutSerializer(about, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
