from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from rest_framework.response import Response

from rest_framework.views import APIView

from .models import User
# from .serializer import AuthUserSer

#
# class SignUp(APIView):
#     def get(self, request):
#         ser = AuthUserSer(User.objects.all(), many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         ser = AuthUserSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
