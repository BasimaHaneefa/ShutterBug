from datetime import datetime, timezone
from django.shortcuts import redirect, render
from Guest.models import tbl_user,tbl_photographer
from Admin.models import tbl_photographercategory
from Photographers.models import tbl_addgallery, tbl_post
from User.models import tbl_booking, tbl_complaint, tbl_feedback, tbl_uchat
from django.db.models import Q

# Create your views here.

#####################HomePage######################################

def Home(request):
    if 'uid' in request.session:
        return render(request,"User/HomePage.html")
    else:
        return render(request,"Guest/Login.html")
    
####################Myprofile#####################################
    
def Myprofile(request):
    if 'uid' in request.session:
        profile=tbl_user.objects.get(id=request.session["uid"])
        return render(request,"User/MyProfile.html",{'profile':profile})
    else:
        return render(request,"Guest/Login.html")
    
####################Editprofile###################################
    
def EditProfile(request):
    if 'uid' in request.session:
        profile=tbl_user.objects.get(id=request.session["uid"])
        if request.method=="POST":
            profile.user_name=request.POST.get("txtusername")
            profile.user_email=request.POST.get("txtusertemail")
            profile.user_contact=request.POST.get("txtusercontact")
            profile.user_address=request.POST.get("txtuseraddress")
            profile.save()
            return redirect("User:Myprofile")
        else:
            return render(request,"User/EditProfile.html",{'profile':profile})
    else:
        return render(request,"Guest/Login.html")
    
########################Changepassword############################################
    
def Changpassword(request):
    if 'uid' in request.session:
        if request.method=="POST":
            Current=request.POST.get("userpwd")
            New=request.POST.get("nuserpwd")
            repass=request.POST.get("cuserpwd")
            profile=tbl_user.objects.get(id=request.session["uid"])
            password=profile.user_password
            if Current == password:
                if New == repass:
                    profile.user_password=New
                    profile.save()
                    return redirect("User:Myprofile")
                else:
                    msg="Password mismatch "
                    return render(request,"User/ChangePassword.html",{'msg':msg})
            else:
                msg="Invalid old password"
                return render(request,"User/ChangePassword.html",{'msg':msg})
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return render(request,"Guest/Login.html")
    
###############################SearchPhotographer##########################
    
def SearchPhotographer(request):
    cat=tbl_photographercategory.objects.all()
    data=tbl_photographer.objects.filter(photographer_vstatus=1)
    return render(request,"User/SearchPhotographer.html",{'cat':cat,'data':data})
    
def Ajaxsearch(request):
    cat=tbl_photographercategory.objects.get(id=request.GET.get("disd"))
    data=tbl_photographer.objects.filter(photographer_vstatus=1,pcat=cat)
    return render(request,"User/Ajaxsearchphotographer.html",{'data':data})

def Viewpost(request,pid):
    photographerid=tbl_photographer.objects.get(id=pid)
    data=tbl_post.objects.filter(photographer=photographerid)
    return render(request,"User/ViewPost.html",{'post':data})

def Viewgallery(request,gid):
    postid=tbl_post.objects.get(id=gid)
    gallery=tbl_addgallery.objects.filter(post=postid)
    return render(request,"User/ViewGallery.html",{'gallery':gallery})

def PhotographerBooking(request,pid):
    if request.method=="POST":
        pid=tbl_photographer.objects.get(id=pid)
        uid=tbl_user.objects.get(id=request.session["uid"])
        tbl_booking.objects.create(photographer=pid,
                                    booking_date=request.POST.get("date"),
                                    booking_description=request.POST.get("txtdescription"),
                                    user=uid)
        return redirect("User:SearchPhotographer")
    else:
        return render(request,"User/PhotographerBooking.html")
    
def ViewPhotographerBooking(request):
    uid=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_booking.objects.filter(user=uid)
    return render(request,"User/ViewMyBooking.html",{'data':data})


#############################Complaint#####################################################

def Complaint(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_complaint.objects.filter(user=userdata)
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session["uid"])
        tbl_complaint.objects.create(complaint_title=request.POST.get("title"),
                                     complaint_content=request.POST.get("complaint"),
                                     user=userdata)
    return render(request,"User/Complaint.html",{"Data":data})

def DelComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:complaint")

def EditComplaint(request,eid):
    com=tbl_complaint.objects.get(id=eid)
    if request.method=="POST":
        com.complaint_title=request.POST.get("title")
        com.complaint_content=request.POST.get("complaint")
        com.save()
        return redirect("User:complaint")
    else:
        return render(request,"User/Complaint.html",{"com":com})
    
########################Feedback############################################
    
def Feedback(request):
    userdata=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_feedback.objects.filter(user=userdata)
    if request.method=="POST":
        userdata=tbl_user.objects.get(id=request.session["uid"])
        tbl_feedback.objects.create(feedback_content=request.POST.get("complaint"),
                                     user=userdata)
    return render(request,"User/Feedback.html",{"Data":data})

def DelFeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("User:feedback")

def EditFeedback(request,eid):
    com=tbl_feedback.objects.get(id=eid)
    if request.method=="POST":
        com.feedback_content=request.POST.get("complaint")
        com.save()
        return redirect("User:feedback")
    else:
        return render(request,"User/Feedback.html",{"com":com})
    
############################Chat#######################################################
    
def chatpage(request,id):
    if 'uid' in request.session:
        photographer  = tbl_photographer.objects.get(id=id)
        return render(request,"User/Chat.html",{"photographer":photographer})
    else:
        return redirect("Guest:Login")

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_user = tbl_user.objects.get(id=request.session["uid"])
            to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_uchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,photographer_to=to_photographer,chat_file=request.FILES.get("file"))
            return render(request,"User/Chat.html")
        else:
            from_user = tbl_user.objects.get(id=request.session["uid"])
            to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
            print(timezone.now())
            tbl_uchat.objects.create(chat_content="",chat_time=datetime.now(),user_from=from_user,photographer_to=to_photographer,chat_file=request.FILES.get("file"))
            return render(request,"User/Chat.html")
    else:
        from_user = tbl_user.objects.get(id=request.session["uid"])
        to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        print(timezone.now())
        tbl_uchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,photographer_to=to_photographer,chat_file="")
        return render(request,"User/Chat.html")
    
def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_uchat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(photographer_from=tid) | Q(photographer_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_uchat.objects.filter(Q(user_from=request.session["uid"]) & Q(photographer_to=request.GET.get("tid")) | (Q(photographer_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

# ##########################Logout################################################

# def logout(request):
#     if 'uid' in request.session:
#         del request.session['uid']
#         return redirect('Guest:Login')
#     else:
#         return redirect('Guest:Login')
