from django.http import response
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from . import smartcontract
from api.models import Voterdb

# Create your views here.
def adminloginpage(request):
    if not request.user.is_authenticated:
        return render(request,'adminlogin.html')
    elif request.user.is_authenticated and request.user.is_superuser==False:
        return render(request,'adminlogin.html')
    else:
        return redirect('/dashboard/')

def adminauthenticate(request):
    #function to authenticate admin login
    username=request.POST['username']
    password=request.POST['password']
    #authentication
    user = authenticate(username=username, password=password)
    #if the user exists
    if user is not None and user.is_superuser==True:
        #login code
        login(request,user)
        return redirect('/dashboard/')
    #if the user does not exist
    elif user is None:
        messages.add_message(request,messages.ERROR,"Invalid credentials")
        return redirect ('/')
    else:
        messages.add_message(request,messages.ERROR,"Superuser account needed")
        return redirect ('/')
def admindashboard(request):
    if not request.user.is_authenticated:
        return redirect("/")
    elif request.user.is_authenticated and request.user.is_superuser==False:
        return redirect("/")
    else:
        return render(request,'dashboard.html')
def adminlogout(request):
    #code for logout from admin panel
    logout(request)
    return redirect('/')

def smartcontractview(request):
    candidatesarray = smartcontract.getdata()
    count = smartcontract.getcount()
    candidatenamearray = []
    candidatevotecountarray = []
    for i in range(count):
        candidatenamearray.append(candidatesarray[i][1])
    for i in range(count):
        candidatevotecountarray.append(candidatesarray[i][2])
    context = {"candidatenames": candidatenamearray, "votecounts": candidatevotecountarray}
    return render(request,'smartcontract.html',context)

def checksignerview(request):
    return render(request,"signerstatus.html")

def checksigner(request):
    address = request.POST['address']
    status = smartcontract.getsignerstatus(address)
    context= {"status" : status, "address":address}
    return render(request, "signerstatus.html",context)

def checkvoterdbview(request):
    return render(request,'searchvoterdb.html')

def voterdata(request):
    voter_id = request.POST['voterid'].upper()
    if Voterdb.objects.filter(Voter_id = voter_id).exists():
        exist = True
        voter_data = Voterdb.objects.get(Voter_id=voter_id)
        context = {
        "exist": exist,
        "id": voter_data.id,
        "firstname": voter_data.firstname,
        "lastname": voter_data.lastname,
        "voter_id": voter_data.Voter_id,
        "phone": voter_data.phone,
        "voting_status": voter_data.voting_status,
        "voter_address": voter_data.voter_address,
        "txn_hash": voter_data.txn_hash
        }
        return render(request,"searchvoterdb.html",context)
    else:
        exist = True
        context = {"not_exist": exist}
        return render(request,"searchvoterdb.html",context)
    