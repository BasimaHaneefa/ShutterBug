from datetime import datetime, timezone
from django.shortcuts import redirect, render
from Guest.models import tbl_model
from Models.models import *
from Photographers.models import tbl_mbooking
from django.db.models import Q
# Create your views here.

#####################HomePage######################################

def Home(request):
    if 'mid' in request.session:
        return render(request,"Models/HomePage.html")
    else:
        return render(request,"Guest/Login.html")
    
####################Myprofile#####################################
    
def Myprofile(request):
    if 'mid' in request.session:
        profile=tbl_model.objects.get(id=request.session["mid"])
        return render(request,"Models/MyProfile.html",{'profile':profile})
    else:
        return render(request,"Guest/Login.html")
    
####################Editprofile###################################
    
def EditProfile(request):
    if 'mid' in request.session:
        profile=tbl_model.objects.get(id=request.session["mid"])
        if request.method=="POST":
            profile.model_name=request.POST.get("txtmodelname")
            profile.model_email=request.POST.get("txtmodeltemail")
            profile.model_contact=request.POST.get("txtmodelcontact")
            profile.model_address=request.POST.get("txtmodeladdress")
            profile.save()
            return redirect("Models:Myprofile")
        else:
            return render(request,"Models/EditProfile.html",{'profile':profile})
    else:
        return render(request,"Guest/Login.html")
    
########################Changepassword############################################
    
def Changpassword(request):
    if 'mid' in request.session:
        if request.method=="POST":
            Current=request.POST.get("modelpwd")
            New=request.POST.get("nmodelpwd")
            repass=request.POST.get("cmodelpwd")
            profile=tbl_model.objects.get(id=request.session["mid"])
            password=profile.model_password
            if Current == password:
                if New == repass:
                    profile.model_password=New
                    profile.save()
                    return redirect("Models:Myprofile")
                else:
                    msg="Password mismatch "
                    return render(request,"Models/ChangePassword.html",{'msg':msg})
            else:
                msg="Invalid old password"
                return render(request,"Models/ChangePassword.html",{'msg':msg})
        else:
            return render(request,"Models/ChangePassword.html")
    else:
        return render(request,"Guest/Login.html")
    
############################ModelPost###############################################
    
def Modelpost(request):
    mid=tbl_model.objects.get(id=request.session["mid"])
    post=tbl_modelpic.objects.filter(model=mid)
    if request.method=="POST":
        tbl_modelpic.objects.create(post_image=request.FILES.get("img"),
                                    post_caption=request.POST.get("txtcaption"),
                                    model=mid)
        return render(request,"Models/ModelPost.html",{'post':post})
    else:
        return render(request,"Models/ModelPost.html",{'post':post})
    
def Deletemodelpost(request,did):
    tbl_modelpic.objects.get(id=did).delete()
    return redirect("Models:Modelpost")
    
########################ViewPhotographerBooking######################################

def ViewPhotographerBooking(request):
    mid=tbl_model.objects.get(id=request.session["mid"])
    mdata=tbl_mbooking.objects.filter(model=mid,mbooking_vstatus=0)
    return render(request,"Models/ViewPhotographerBooking.html",{'data':mdata})

def accept(request,aid):
    data=tbl_mbooking.objects.get(id=aid)
    data.mbooking_vstatus=1
    data.save()
    return redirect("Models:ViewPhotographerBooking")

def reject(request,rid):
    data=tbl_mbooking.objects.get(id=rid)
    data.mbooking_vstatus=2
    data.save()
    return redirect("Models:ViewPhotographerBooking")

def AcceptedBooking(request):
    pdata=tbl_model.objects.get(id=request.session["mid"])
    accdata=tbl_mbooking.objects.filter(model=pdata,mbooking_vstatus=1)
    return render(request,"Models/AcceptedBooking.html",{'acc':accdata})

def RejectedBooking(request):
    pdata=tbl_model.objects.get(id=request.session["mid"])
    rejdata=tbl_mbooking.objects.filter(model=pdata,mbooking_vstatus=2)
    return render(request,"Models/RejectedBooking.html",{'rej':rejdata})

############################Chat#######################################################
    
def chatpage(request,id):
    if 'mid' in request.session:
        photographer  = tbl_photographer.objects.get(id=id)
        return render(request,"Models/Chat.html",{"photographer":photographer})
    else:
        return redirect("Guest:Login")

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_model = tbl_model.objects.get(id=request.session["mid"])
            to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_mchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),model_from=from_model,photographer_to=to_photographer,chat_file=request.FILES.get("file"))
            return render(request,"Models/Chat.html")
        else:
            from_model = tbl_model.objects.get(id=request.session["mid"])
            to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
            print(timezone.now())
            tbl_mchat.objects.create(chat_content="",chat_time=datetime.now(),model_from=from_model,photographer_to=to_photographer,chat_file=request.FILES.get("file"))
            return render(request,"Models/Chat.html")
    else:
        from_model = tbl_model.objects.get(id=request.session["mid"])
        to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        print(timezone.now())
        tbl_mchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),model_from=from_model,photographer_to=to_photographer,chat_file="")
        return render(request,"Models/Chat.html")
    
def ajaxchatview(request):
    tid = request.GET.get("tid")
    model = tbl_model.objects.get(id=request.session["mid"])
    chat_data = tbl_mchat.objects.filter((Q(model_from=model) | Q(model_to=model)) & (Q(photographer_from=tid) | Q(photographer_to=tid))).order_by('chat_time')
    return render(request,"Models/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_mchat.objects.filter(Q(model_from=request.session["mid"]) & Q(photographer_to=request.GET.get("tid")) | (Q(photographer_from=request.GET.get("tid")) & Q(model_to=request.session["mid"]))).delete()
    return render(request,"Models/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

