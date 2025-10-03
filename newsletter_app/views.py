from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import NewsletterModel

class NewsletterView(APIView):

    def post(self, request):
        
        try:
            email = request.data.get('email')
            if not email:
                return Response({'error' : 'email not found.'}, status=status.HTTP_404_NOT_FOUND)
            
            birth_year = request.data.get('year')
            if not birth_year:
                return Response({'error' : 'birth year not found.'}, status=status.HTTP_404_NOT_FOUND)
            
            birth_month = request.data.get('month')
            if not birth_month:
                return Response({'error' : 'birth month not found.'}, status=status.HTTP_404_NOT_FOUND)
            
            birth_day = request.data.get('day')
            if not birth_day:
                return Response({'error' : 'birth day not found.'}, status=status.HTTP_404_NOT_FOUND)
            
            NewsletterModel.objects.create(
                email=email,
                birth_year = birth_year,
                birth_month = birth_month,
                birth_day=birth_day,
            )
            return Response({'message' : 'newsletter created successfuly.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)