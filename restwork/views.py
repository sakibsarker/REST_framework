from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Advocate
from .serializers import AdvocateSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def enpoint(request):
    data=['advocates','advocates/:username']
    return Response(data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def advocate_list(request):
    if request.method=='GET':
        query=request.GET.get('query')
        if query==None:
            query=''
        advocate=Advocate.objects.filter(Q(username__icontains=query)|Q(bio__icontains=query))
        serializer=AdvocateSerializer(advocate,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        advocate=Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio']
        )
        serializer=AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    

# @permission_classes([IsAuthenticatedOrReadOnly])
# class AdvocateDetails(APIView):
#     def get(self, request, username):
#         try:
#             advocate=Advocate.objects.get(username=username)
#             serializer=AdvocateSerializer(advocate,many=False)
#             return Response(serializer.data)
#         except ObjectDoesNotExist:
#             return Response({'error': 'Advocate username not found.'}, status=404)
#     def put(self,request,username):
#         advocate=Advocate.objects.get(username=username)
#         advocate.bio=request.data['bio']
#         advocate.save()
#         serializer=AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)
#     def delete(self,request,username):
#         advocate=Advocate.objects.get(username=username)
#         advocate.delete()
#         return Response('user was deleted')

    
        

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def advocate_details(request,username):
    try:
        advocate=Advocate.objects.get(username=username)
        if request.method=="GET":
            serializer=AdvocateSerializer(advocate,many=False)
            return Response(serializer.data)
        if request.method=='PUT':
            advocate.username=request.data['username']
            advocate.bio=request.data['bio']
            advocate.save()
            serializer=AdvocateSerializer(advocate,many=False)
            return Response(serializer.data)
        if request.method=='DELETE':
            advocate.delete()
            return Response('delete done')
    except ObjectDoesNotExist:
        return Response({'error': 'Advocate username not found.'}, status=404)