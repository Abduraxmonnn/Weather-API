# Rest-Framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Project
from apps.user.serializers import UserSignInSerializer


class UserSignInView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSignInSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            return Response({
                'user': {
                    'username': data['user'].username,
                    'name': data['user'].name,
                    'surname': data['user'].surname,
                    'is_active': data['user'].is_active,
                },
                'token': data['token']
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
