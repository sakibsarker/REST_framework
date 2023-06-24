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
from django.http import Http404

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
    

@permission_classes([IsAuthenticatedOrReadOnly])
class AdvocateDetails(APIView):
    def get_object(self,username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise Http404
    def get(self, request, username):
        advocate=self.get_object(username)
        serializer=AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    def put(self,request,username):
        advocate=self.get_object(username)
        advocate.username=request.data['username']
        advocate.bio=request.data['bio']
        advocate.save()
        serializer=AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    def delete(self,request,username):
        advocate=self.get_object(username)
        advocate.delete()
        return Response('user was deleted')


