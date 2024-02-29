from datetime import datetime
from django.shortcuts import redirect, render
from Guest.models import tbl_photographer,tbl_model, tbl_user
from Photographers.models import *
from Admin.models import tbl_editorcategory
from Models.models import tbl_mchat, tbl_modelpic
from User.models import tbl_booking, tbl_uchat
from django.db.models import Q
# Create your views here.

#####################HomePage######################################

def Home(request):
    if 'pid' in request.session:
        return render(request,"Photographers/HomePage.html")
    else:
        return render(request,"Guest/Login.html")
    
####################Myprofile#####################################
    
def Myprofile(request):
    if 'pid' in request.session:
        profile=tbl_photographer.objects.get(id=request.session["pid"])
        return render(request,"Photographers/MyProfile.html",{'profile':profile})
    else:
        return render(request,"Guest/Login.html")
    
####################Editprofile###################################
    
def EditProfile(request):
    if 'pid' in request.session:
        profile=tbl_photographer.objects.get(id=request.session["pid"])
        if request.method=="POST":
            profile.photographer_name=request.POST.get("txtphotographername")
            profile.photographer_email=request.POST.get("txtphotographertemail")
            profile.photographer_contact=request.POST.get("txtphotographercontact")
            profile.photographer_address=request.POST.get("txtphotographeraddress")
            profile.save()
            return redirect("Photographers:Myprofile")
        else:
            return render(request,"Photographers/EditProfile.html",{'profile':profile})
    else:
        return render(request,"Guest/Login.html")
    
########################Changepassword############################################
    
def Changpassword(request):
    if 'pid' in request.session:
        if request.method=="POST":
            Current=request.POST.get("photographerpwd")
            New=request.POST.get("nphotographerpwd")
            repass=request.POST.get("cphotographerpwd")
            profile=tbl_photographer.objects.get(id=request.session["pid"])
            password=profile.photographer_password
            if Current == password:
                if New == repass:
                    profile.photographer_password=New
                    profile.save()
                    return redirect("Photographers:Myprofile")
                else:
                    msg="Password mismatch "
                    return render(request,"Photographers/ChangePassword.html",{'msg':msg})
            else:
                msg="Invalid old password"
                return render(request,"Photographers/ChangePassword.html",{'msg':msg})
        else:
            return render(request,"Photographers/ChangePassword.html")
    else:
        return render(request,"Guest/Login.html")
    
###########################POST######################################################
    
def Post(request):
    if 'pid' in request.session:
        pdata=tbl_photographer.objects.get(id=request.session["pid"])
        post=tbl_post.objects.filter(photographer=pdata)
        if request.method=="POST":
            tbl_post.objects.create(post_name=request.POST.get("txttitle"),
                                post_caption=request.POST.get("txtcaption"),
                                post_image=request.FILES.get("img"),
                                post_amount=request.POST.get("txtamount"),
                                photographer=pdata)
            return render(request,"Photographers/Post.html",{'post':post})
        else:
            return render(request,"Photographers/Post.html",{'post':post})
    else:
        return render(request,"Guest/Login.html")
    
def Deletepost(request,did):
    tbl_post.objects.get(id=did).delete()
    return redirect("Photographers:Post")

def Addgallery(request,gid):
    postid=tbl_post.objects.get(id=gid)
    gallery=tbl_addgallery.objects.filter(post=postid)
    if request.method=="POST":
        tbl_addgallery.objects.create(addgallery_caption=request.POST.get("txtcaption"),
                                      addgallery_image=request.FILES.get("img"),
                                      post=postid)
        return render(request,"Photographers/Addgallery.html",{'gallery':gallery})
    else:
        return render(request,"Photographers/Addgallery.html",{'gallery':gallery})
    
def Deletegallery(request,did):
    tbl_addgallery.objects.get(id=did).delete()
    return redirect("Photographers:Post")

###########################Search Editor##############################################

def SearchEditor(request):
    cat=tbl_editorcategory.objects.all()
    editor=tbl_editor.objects.filter(editor_vstatus=1)
    return render(request,"Photographers/SearchEditor.html",{'cat':cat,'editor':editor})

def Ajaxeditorsearch(request):
    cat=tbl_editorcategory.objects.get(id=request.GET.get("disd"))
    editor=tbl_editor.objects.filter(ecat=cat,editor_vstatus=1)
    return render(request,"Photographers/Ajaxsearcheditor.html",{'editor':editor})

def Viewmore(request,eid):
    editor=tbl_editor.objects.get(id=eid)
    post=tbl_post.objects.filter(editor=editor)
    return render(request,"Photographers/Viewmore.html",{'post':post})

def Viewgallery(request,gid):
    postid=tbl_post.objects.get(id=gid)
    gallery=tbl_addgallery.objects.filter(post=postid)
    return render(request,"Photographers/ViewGallery.html",{'gallery':gallery})

def EditorBooking(request,eid):
    if request.method=="POST":
        editorid=tbl_editor.objects.get(id=eid)
        pid=tbl_photographer.objects.get(id=request.session["pid"])
        tbl_ebooking.objects.create(editor=editorid,
                                    booking_date=request.POST.get("date"),
                                    ebooking_discription=request.POST.get("txtdescription"),
                                    photographer=pid)
        return redirect("Photographers:SearchEditor")
    else:
        return render(request,"Photographers/EditorBooking.html")
    
def ViewEditorBooking(request):
    pid=tbl_photographer.objects.get(id=request.session["pid"])
    data=tbl_ebooking.objects.filter(photographer=pid)
    return render(request,"Photographers/ViewMyBooking.html",{'data':data})

##############################SearchModel####################################

def SearchModel(request):
    mdata=tbl_model.objects.all()
    return render(request,"Photographers/SearchModeling.html",{'data':mdata})

def Ajaxsearchmodel(request):
    sdata = None  
    if 'search' in request.GET and request.GET['search']:  
        search = request.GET['search']
        sdata = tbl_model.objects.filter(model_name__icontains=search)  

    return render(request, "Photographers/Ajaxsearchmodel.html", {'data': sdata})

def Viewmodelpost(request,pid):
    mdata=tbl_model.objects.get(id=pid)
    data=tbl_modelpic.objects.filter(model=mdata)
    return render(request, "Photographers/ViewPost.html",{'data':data})

def ModelBooking(request,mid):
    if request.method=="POST":
        modelid=tbl_model.objects.get(id=mid)
        pid=tbl_photographer.objects.get(id=request.session["pid"])
        tbl_mbooking.objects.create(model=modelid,
                                    booking_date=request.POST.get("date"),
                                    mbooking_discription=request.POST.get("txtdescription"),
                                    photographer=pid)
        return redirect("Photographers:SearchModel")
    else:
        return render(request,"Photographers/ModelBooking.html")
    
def ViewModelBooking(request):
    pid=tbl_photographer.objects.get(id=request.session["pid"])
    data=tbl_mbooking.objects.filter(photographer=pid)
    return render(request,"Photographers/ViewMyModelBooking.html",{'data':data})

##########################ViewUserBooking#######################################

def ViewUserBooking(request):
    pid=tbl_photographer.objects.get(id=request.session["pid"])
    data=tbl_booking.objects.filter(photographer=pid,booking_vstatus=0)
    return render(request,"Photographers/ViewUserBooking.html",{'data':data})

def accept(request,aid):
    data=tbl_booking.objects.get(id=aid)
    data.booking_vstatus=1
    data.save()
    return redirect("Photographers:ViewUserBooking")

def reject(request,rid):
    data=tbl_booking.objects.get(id=rid)
    data.booking_vstatus=2
    data.save()
    return redirect("Photographers:ViewUserBooking")

def AcceptedBooking(request):
    pdata=tbl_photographer.objects.get(id=request.session["pid"])
    accdata=tbl_booking.objects.filter(photographer=pdata,booking_vstatus=1)
    return render(request,"Photographers/AcceptedBooking.html",{'acc':accdata})

def RejectedBooking(request):
    pdata=tbl_photographer.objects.get(id=request.session["pid"])
    rejdata=tbl_booking.objects.filter(photographer=pdata,booking_vstatus=2)
    return render(request,"Photographers/RejectedBooking.html",{'rej':rejdata})

########################UserChat################################################

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Photographers/Chat.html",{"user":user})

def ajaxchat(request):
    # print(request.POST.get("tid"))
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_uchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),photographer_from=from_photographer,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"Photographers/Chat.html")
        else:
            from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
            to_user = tbl_user.objects.get(id=request.POST.get("tid"))
            tbl_uchat.objects.create(chat_content="",chat_time=datetime.now(),photographer_from=from_photographer,user_to=to_user,chat_file=request.FILES.get("file"))
            return render(request,"Photographers/Chat.html")
    else:
        from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
        to_user = tbl_user.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        tbl_uchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),photographer_from=from_photographer,user_to=to_user,chat_file="")
        return render(request,"Photographers/Chat.html")
    
def ajaxchatview(request):
    tid = request.GET.get("tid")
    photographer = tbl_photographer.objects.get(id=request.session["pid"])
    chat_data = tbl_uchat.objects.filter((Q(photographer_from=photographer) | Q(photographer_to=photographer)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Photographers/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_uchat.objects.filter(Q(photographer_from=request.session["pid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(photographer_to=request.session["pid"]))).delete()
    return render(request,"Photographers/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

########################################EditorChat###########################################################

def echatpage(request,id):
    editor  = tbl_editor.objects.get(id=id)
    return render(request,"Photographers/EChat.html",{"editor":editor})

def ajaxechat(request):
    # print(request.POST.get("tid"))
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
            to_editor = tbl_editor.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),photographer_from=from_photographer,editor_to=to_editor,chat_file=request.FILES.get("file"))
            return render(request,"Photographers/EChat.html")
        else:
            from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
            to_user = tbl_editor.objects.get(id=request.POST.get("tid"))
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),photographer_from=from_photographer,editor_to=to_editor,chat_file=request.FILES.get("file"))
            return render(request,"Photographers/EChat.html")
    else:
        from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
        to_editor = tbl_editor.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),photographer_from=from_photographer,editor_to=to_editor,chat_file="")
        return render(request,"Photographers/EChat.html")
    
def ajaxechatview(request):
    tid = request.GET.get("tid")
    photographer = tbl_photographer.objects.get(id=request.session["pid"])
    chat_data = tbl_chat.objects.filter((Q(photographer_from=photographer) | Q(photographer_to=photographer)) & (Q(editor_from=tid) | Q(editor_to=tid))).order_by('chat_time')
    return render(request,"Photographers/EChatView.html",{"data":chat_data,"tid":int(tid)})

def eclearchat(request):
    tbl_chat.objects.filter(Q(photographer_from=request.session["pid"]) & Q(editor_to=request.GET.get("tid")) | (Q(editor_from=request.GET.get("tid")) & Q(photographer_to=request.session["pid"]))).delete()
    return render(request,"Photographers/EClearChat.html",{"msg":"Chat Deleted Sucessfully...."})


########################################ModelChat###########################################################

def mchatpage(request,id):
    model  = tbl_model.objects.get(id=id)
    return render(request,"Photographers/MChat.html",{"model":model})

def ajaxmchat(request):
    # print(request.POST.get("tid"))
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
            to_model = tbl_model.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_mchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),photographer_from=from_photographer,model_to=to_model,chat_file=request.FILES.get("file"))
            return render(request,"Photographers/MChat.html")
        else:
            from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
            to_model = tbl_model.objects.get(id=request.POST.get("tid"))
            tbl_mchat.objects.create(chat_content="",chat_time=datetime.now(),photographer_from=from_photographer,model_to=to_model,chat_file=request.FILES.get("file"))
            return render(request,"Photographers/MChat.html")
    else:
        from_photographer = tbl_photographer.objects.get(id=request.session["pid"])
        to_model = tbl_model.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        tbl_mchat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),photographer_from=from_photographer,model_to=to_model,chat_file="")
        return render(request,"Photographers/MChat.html")
    
def ajaxmchatview(request):
    tid = request.GET.get("tid")
    photographer = tbl_photographer.objects.get(id=request.session["pid"])
    chat_data = tbl_mchat.objects.filter((Q(photographer_from=photographer) | Q(photographer_to=photographer)) & (Q(model_from=tid) | Q(model_to=tid))).order_by('chat_time')
    return render(request,"Photographers/MChatView.html",{"data":chat_data,"tid":int(tid)})

def mclearchat(request):
    tbl_mchat.objects.filter(Q(photographer_from=request.session["pid"]) & Q(model_to=request.GET.get("tid")) | (Q(model_from=request.GET.get("tid")) & Q(photographer_to=request.session["pid"]))).delete()
    return render(request,"Photographers/MClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

# ##########################Logout################################################

# def logout(request):
#     if 'pid' in request.session:
#         del request.session['pid']
#         return redirect('Guest:Login')
#     else:
#         return redirect('Guest:Login')

