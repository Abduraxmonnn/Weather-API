# Rest-Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Project
from apps.user.models import User
from apps.user.serializers import UserSignUpSerializer


class UserSignUpViewSet(viewsets.ModelViewSet):
    model = User
    queryset = model.objects.all()
    serializer_class = UserSignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()

            return Response({
                'user': {
                    'username': data['user'].username,
                    'name': data['user'].name,
                    'surname': data['user'].surname,
                    'is_active': data['user'].is_active,
                },
                'token': data['token']
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
