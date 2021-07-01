from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from member.models import MemberVO
from member.serializers import MemberSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework import serializers
from icecream import ic


@api_view(['GET', 'POST', 'DELETE'])
@parser_classes([JSONParser])
def members(request):
    print('-----여기까지 왔다--------')
    if request.method == 'GET':
        all_members = MemberVO.objects.all()
        ic(all_members)
        serializer = MemberSerializer(all_members, many=True)
        ic(type(serializer.data))
        ic(serializer.data)
        return JsonResponse(serializer.data, safe=False)

        '''
        data = serializers.serialize('json', all_members)
        ic(data)
        return Response(data=data, status=201)
        '''
        '''
        ic(all_members)
        serializer = MemberSerializer(all_members, many=True)
        ic(type(serializer.data))
        ic(serializer.data)
        return JsonResponse(serializer.data, safe=False)
        '''
    elif request.method == 'POST':
        new_member = request.data['body']
        ic(new_member)
        serializer = MemberSerializer(data=new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'PUT', 'DELETE'])
def member(request, pk):
    if request.method == 'GET':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)