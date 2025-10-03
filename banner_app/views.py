from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BannerModel
from .serializers import BannerSerializer



class BannerListView(APIView):
    def get(self, request):
        try:
            banners = BannerModel.objects.all()
            serializer = BannerSerializer(banners, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
