from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import BoardVO
from .serializers import BoardSerializer
from rest_framework.views import APIView
from icecream import ic
from rest_framework.response import Response


class Boards(APIView):
    def post(self, request):
        data = request.data['body']
        ic(data)
        serializer = BoardSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'result': 'success'})
        ic(serializer.errors)
        return Response(serializer.errors, status=400)
