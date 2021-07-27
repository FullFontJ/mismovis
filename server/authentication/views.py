from django.http import response
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.views import APIView

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return response(status=status.HTTP_200_OK)

        return response(status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    def post(self, request):
        logout(request)

        return response(status=status.HTTP_200_OK)