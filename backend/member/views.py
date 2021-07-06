from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status
from member.models import MemberVO
from member.serializers import MemberSerializer
from rest_framework.decorators import api_view, parser_classes
from icecream import ic
# import datetime
# from rest_framework.response import Response


@api_view(['GET', 'POST'])
def members(request):
    if request.method == 'GET':
        all_members = MemberVO.objects.all()
        serializer = MemberSerializer(all_members, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        new_member = request.data['body']
        ic(new_member)
        serializer = MemberSerializer(data=new_member)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result': f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def member(request):
    if request.method == 'GET':
        serializer = MemberSerializer()
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'DELETE':
        data = request.data['body']
        ic(data)
        pk = data['member']['username']
        user_input_password = data['member']['password']
        member = MemberVO.objects.get(pk=pk)
        if user_input_password == member.password:
            member.delete()
            return JsonResponse({'result': 'SUCCESS'}, safe=False)
        else:
            print('비밀번호가 다릅니다')
            return JsonResponse({'result': 'PASSWORD-FAIL'}, status=201)

@api_view(['PUT'])
def member_modify(request):
    data = request.data['body']
    update_member = data['member']
    ic(update_member)
    pk = update_member['username']
    member = MemberVO.objects.get(pk=pk)
    user_change_password = update_member['password']
    ic(user_change_password)
    serializer = MemberSerializer(member, data=data['member'], partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'result': f'Update Success , {serializer.data.get("name")}'}, status=201)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    try:
        data = request.data['body']
        pk = data['username']
        user_input_password = data['password']
        member = MemberVO.objects.get(pk=pk)
        ic(member)
        if user_input_password == member.password:
            serializer = MemberSerializer(member, many=False)
            return JsonResponse(data=serializer.data, safe=False)
        else:
            print('비밀번호가 다릅니다')
            return JsonResponse({'result': 'PASSWORD-FAIL'}, status=201)
    except MemberVO.DoesNotExist:
        return JsonResponse({'result': "USERNAME-FAIL"}, status=201)
    return HttpResponse(status=104)











