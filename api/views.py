from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import VoterdbSerializer

# Create your views here.
@api_view(['GET'])
def getdata(request,voterid):
    data = Voterdb.objects.filter(Voter_id = voterid)
    serializer = VoterdbSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getvotingstatus(request,voterid):
    data = Voterdb.objects.get(Voter_id = voterid)
    context = {'voting_status' : data.voting_status}
    return Response(context)

@api_view(['GET'])
def getauthphone(request,voterid):
    data = Voterdb.objects.get(Voter_id = voterid)
    context = {'phone' : data.phone, 'Voter_id': data.Voter_id}
    return Response(context)

# @api_view(['POST'])
# def create_user(request):
#     serializer = VoterdbSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

@api_view(['PUT'])
def change_status(request,voterid):
    votedata = Voterdb.objects.get(Voter_id=voterid)
    serializer = VoterdbSerializer(votedata,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



