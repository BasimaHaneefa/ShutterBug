from datetime import datetime, timezone
from django.shortcuts import redirect, render
from Guest.models import tbl_editor, tbl_photographer
from Photographers.models import tbl_addgallery, tbl_chat,tbl_post,tbl_ebooking
from django.db.models import Q

# Create your views here.

#####################HomePage######################################

def Home(request):
    if 'eid' in request.session:
        return render(request,"Editors/HomePage.html")
    else:
        return render(request,"Guest/Login.html")
    
####################Myprofile#####################################
    
def Myprofile(request):
    if 'eid' in request.session:
        profile=tbl_editor.objects.get(id=request.session["eid"])
        return render(request,"Editors/MyProfile.html",{'profile':profile})
    else:
        return render(request,"Guest/Login.html")
    
####################Editprofile###################################
    
def EditProfile(request):
    if 'eid' in request.session:
        profile=tbl_editor.objects.get(id=request.session["eid"])
        if request.method=="POST":
            profile.editor_name=request.POST.get("txteditorname")
            profile.editor_email=request.POST.get("txteditortemail")
            profile.editor_contact=request.POST.get("txteditorcontact")
            profile.editor_address=request.POST.get("txteditoraddress")
            profile.save()
            return redirect("Editors:Myprofile")
        else:
            return render(request,"Editors/EditProfile.html",{'profile':profile})
    else:
        return render(request,"Guest/Login.html")
    
########################Changepassword############################################
    
def Changpassword(request):
    if 'eid' in request.session:
        if request.method=="POST":
            Current=request.POST.get("editorpwd")
            New=request.POST.get("neditorpwd")
            repass=request.POST.get("ceditorpwd")
            profile=tbl_editor.objects.get(id=request.session["eid"])
            password=profile.editor_password
            if Current == password:
                if New == repass:
                    profile.editor_password=New
                    profile.save()
                    return redirect("Editors:Myprofile")
                else:
                    msg="Password mismatch "
                    return render(request,"Editors/ChangePassword.html",{'msg':msg})
            else:
                msg="Invalid old password"
                return render(request,"Editors/ChangePassword.html",{'msg':msg})
        else:
            return render(request,"Editors/ChangePassword.html")
    else:
        return render(request,"Guest/Login.html")
    
###########################POST######################################################
    
def Post(request):
    if 'eid' in request.session:
        pdata=tbl_editor.objects.get(id=request.session["eid"])
        post=tbl_post.objects.filter(editor=pdata)
        if request.method=="POST":
            tbl_post.objects.create(post_name=request.POST.get("txttitle"),
                                post_caption=request.POST.get("txtcaption"),
                                post_image=request.FILES.get("img"),
                                post_amount=request.POST.get("txtamount"),
                                editor=pdata)
            return render(request,"Editors/Post.html",{'post':post})
        else:
            return render(request,"Editors/Post.html",{'post':post})
    else:
        return render(request,"Guest/Login.html")
    
def Deletepost(request,did):
    tbl_post.objects.get(id=did).delete()
    return redirect("Editors:Post")

def Addgallery(request,gid):
    postid=tbl_post.objects.get(id=gid)
    gallery=tbl_addgallery.objects.filter(post=postid)
    if request.method=="POST":
        tbl_addgallery.objects.create(addgallery_caption=request.POST.get("txtcaption"),
                                      addgallery_image=request.FILES.get("img"),
                                      post=postid)
        return render(request,"Editors/Addgallery.html",{'gallery':gallery})
    else:
        return render(request,"Editors/Addgallery.html",{'gallery':gallery})
    
def Deletegallery(request,did):
    tbl_addgallery.objects.get(id=did).delete()
    return redirect("Editors:Post")

###########################ViewPhotographerBooking########################################

def ViewPhotogarpherBooking(request):
    pdata=tbl_editor.objects.get(id=request.session["eid"])
    newdata=tbl_ebooking.objects.filter(editor=pdata,ebooking_vstatus=0)
    return render(request,"Editors/ViewPhotographerBooking.html",{'new':newdata})

def accept(request,aid):
    data=tbl_ebooking.objects.get(id=aid)
    data.ebooking_vstatus=1
    data.save()
    return redirect("Editors:ViewPhotogarpherBooking")

def reject(request,rid):
    data=tbl_ebooking.objects.get(id=rid)
    data.ebooking_vstatus=2
    data.save()
    return redirect("Editors:ViewPhotogarpherBooking")

def AcceptedBooking(request):
    pdata=tbl_editor.objects.get(id=request.session["eid"])
    accdata=tbl_ebooking.objects.filter(editor=pdata,ebooking_vstatus=1)
    return render(request,"Editors/AcceptedBooking.html",{'acc':accdata})

def RejectedBooking(request):
    pdata=tbl_editor.objects.get(id=request.session["eid"])
    rejdata=tbl_ebooking.objects.filter(editor=pdata,ebooking_vstatus=2)
    return render(request,"Editors/RejectedBooking.html",{'rej':rejdata})

####################################PhotographersChat################################

def chatpage(request,id):
    if 'eid' in request.session:
        photographer  = tbl_photographer.objects.get(id=id)
        return render(request,"Editors/Chat.html",{"photographer":photographer})
    else:
        return redirect("Guest:Login")

def ajaxchat(request):
    file = request.FILES.get("file")
    if file != '':
        if request.POST.get("msg") != '':
            from_editor= tbl_editor.objects.get(id=request.session["eid"])
            to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
            print(request.POST.get("tid"))
            tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),editor_from=from_editor,photographer_to=to_photographer,chat_file=request.FILES.get("file"))
            return render(request,"Editors/Chat.html")
        else:
            from_editor= tbl_editor.objects.get(id=request.session["eid"])
            to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
            print(timezone.now())
            tbl_chat.objects.create(chat_content="",chat_time=datetime.now(),Editor_from=from_editor,photographer_to=to_photographer,chat_file=request.FILES.get("file"))
            return render(request,"Editors/Chat.html")
    else:
        from_editor= tbl_editor.objects.get(id=request.session["eid"])
        to_photographer = tbl_photographer.objects.get(id=request.POST.get("tid"))
        # print(request.POST.get("tid"))
        print(timezone.now())
        tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),Editor_from=from_editor,photographer_to=to_photographer,chat_file="")
        return render(request,"Editors/Chat.html")
    
def ajaxchatview(request):
    tid = request.GET.get("tid")
    editor= tbl_editor.objects.get(id=request.session["eid"])
    chat_data = tbl_chat.objects.filter((Q(editor_from=editor) | Q(editor_to=editor)) & (Q(photographer_from=tid) | Q(photographer_to=tid))).order_by('chat_time')
    return render(request,"Editors/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(editor_from=request.session["eid"]) & Q(photographer_to=request.GET.get("tid")) | (Q(photographer_from=request.GET.get("tid")) & Q(editor_to=request.session["eid"]))).delete()
    return render(request,"Editors/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

