from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import License
from .serializers import LicenseSerializer
from django.utils import timezone


# API to validate a license
@api_view(['POST'])
def validate_license(request):
    key = request.data.get('key')
    
    try:
        license = License.objects.get(key=key, is_active=True)
        if license.expiry_date > timezone.now():
            return Response({'message': 'License is valid.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'License has expired.'}, status=status.HTTP_400_BAD_REQUEST)
    except License.DoesNotExist:
        return Response({'message': 'License not found or inactive.'}, status=status.HTTP_404_NOT_FOUND)

# API to activate a new license
@api_view(['POST'])
def activate_license(request):
    serializer = LicenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'License activated successfully.'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
