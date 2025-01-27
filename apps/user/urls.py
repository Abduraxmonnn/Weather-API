# Django
from django.urls import path

# Project
from apps.user.api import UserSignUpViewSet, UserSignInView

urlpatterns = [
    path('sign/up/', UserSignUpViewSet.as_view({'post': 'create'})),
    path('sign/in/', UserSignInView.as_view()),
]
