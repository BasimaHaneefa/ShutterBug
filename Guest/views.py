from django.shortcuts import redirect, render
from Admin.models import *
from Guest.models import *
# Create your views here.

#####################Index##################################

def index(request):
    return render(request,"Guest/index.html")

####################Photographer############################

def PhotographerReg(request):
    pcat=tbl_photographercategory.objects.all()
    district=tbl_district.objects.all()
    if request.method=="POST":
       sel_pcat=tbl_photographercategory.objects.get(id=request.POST.get("sel_cat"))
       sel_place=tbl_place.objects.get(id=request.POST.get("sel_place"))
       tbl_photographer.objects.create(photographer_name=request.POST.get("txtname"),
                                       photographer_email=request.POST.get("txtemail"),
                                       photographer_contact=request.POST.get("txtcontact"),
                                       photographer_address=request.POST.get("txtaddress"),
                                       photographer_gender=request.POST.get("gender"),
                                       photographer_photo=request.FILES.get("photo"),
                                       photographer_proof=request.FILES.get("proof"),
                                       photographer_password=request.POST.get("photographerpwd"),
                                       pcat=sel_pcat,place=sel_place)
       return render(request,"Guest/PhotographerRegistration.html",{"dist":district,'cat':pcat})
    else:
        return render(request,"Guest/PhotographerRegistration.html",{"dist":district,'cat':pcat})

###################AjaxPlace################################

def Ajaxplace(request):
    seldis=tbl_district.objects.get(id=request.GET.get("disd"))
    place=tbl_place.objects.filter(district=seldis)
    return render(request,"Guest/AjaxPlace.html",{'place':place})

###################EditorReg################################

def EditorReg(request):
    ecat=tbl_editorcategory.objects.all()
    district=tbl_district.objects.all()
    if request.method=="POST":
       sel_pcat=tbl_editorcategory.objects.get(id=request.POST.get("sel_cat"))
       sel_place=tbl_place.objects.get(id=request.POST.get("sel_place"))
       tbl_editor.objects.create(editor_name=request.POST.get("txtname"),
                                editor_email=request.POST.get("txtemail"),
                                editor_contact=request.POST.get("txtcontact"),
                                editor_address=request.POST.get("txtaddress"),
                                editor_gender=request.POST.get("gender"),
                                editor_photo=request.FILES.get("photo"),
                                editor_proof=request.FILES.get("proof"),
                                editor_password=request.POST.get("editorpwd"),
                                ecat=sel_pcat,place=sel_place)
       return render(request,"Guest/EditorRegistration.html",{"dist":district,'cat':ecat})
    else:
        return render(request,"Guest/EditorRegistration.html",{"dist":district,'cat':ecat})
    
##############################ModelReg###################################################
    
def ModelReg(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
       sel_place=tbl_place.objects.get(id=request.POST.get("sel_place"))
       tbl_model.objects.create(model_name=request.POST.get("txtname"),
                                model_email=request.POST.get("txtemail"),
                                model_contact=request.POST.get("txtcontact"),
                                model_address=request.POST.get("txtaddress"),
                                model_gender=request.POST.get("gender"),
                                model_photo=request.FILES.get("photo"),
                                model_proof=request.FILES.get("proof"),
                                model_password=request.POST.get("modelpwd"),
                                place=sel_place)
       return render(request,"Guest/ModelRegistration.html",{"dist":district})
    else:
        return render(request,"Guest/ModelRegistration.html",{"dist":district})
    
##############################UserReg##########################################
    
def UserReg(request):
    district=tbl_district.objects.all()
    if request.method=="POST":
       sel_place=tbl_place.objects.get(id=request.POST.get("sel_place"))
       tbl_user.objects.create(user_name=request.POST.get("txtname"),
                                user_email=request.POST.get("txtemail"),
                                user_contact=request.POST.get("txtcontact"),
                                user_address=request.POST.get("txtaddress"),
                                user_gender=request.POST.get("gender"),
                                user_photo=request.FILES.get("photo"),
                                user_password=request.POST.get("userpwd"),
                                place=sel_place)
       return render(request,"Guest/UserRegistration.html",{"dist":district})
    else:
        return render(request,"Guest/UserRegistration.html",{"dist":district})
    
###########################Login##############################################
    
def Login(request):
    if request.method=="POST":
        Email=request.POST.get("txtemail")
        Password=request.POST.get("pwd")
        acount=tbl_admin.objects.filter(admin_email=Email,admin_password=Password).count()
        pcount=tbl_photographer.objects.filter(photographer_email=Email,photographer_password=Password,photographer_vstatus=1).count()
        ecount=tbl_editor.objects.filter(editor_email=Email,editor_password=Password,editor_vstatus=1).count()
        mcount=tbl_model.objects.filter(model_email=Email,model_password=Password,model_vstatus=1).count()
        ucount=tbl_user.objects.filter(user_email=Email,user_password=Password).count()
        if acount>0:
            adata=tbl_admin.objects.get(admin_email=Email,admin_password=Password)
            request.session["adid"]=adata.id
            request.session["adname"]=adata.admin_name
            return redirect("Admin:Home")
        elif pcount>0:
            pdata=tbl_photographer.objects.get(photographer_email=Email,photographer_password=Password,photographer_vstatus=1)
            request.session["pid"]=pdata.id
            request.session["pname"]=pdata.photographer_name
            return redirect("Photographers:Home")
        elif ecount>0:
            edata=tbl_editor.objects.get(editor_email=Email,editor_password=Password,editor_vstatus=1)
            request.session["eid"]=edata.id
            request.session["ename"]=edata.editor_name
            return redirect("Editors:Home")
        elif mcount>0:
            mdata=tbl_model.objects.get(model_email=Email,model_password=Password,model_vstatus=1)
            request.session["mid"]=mdata.id
            request.session["mname"]=mdata.model_name
            return redirect("Models:Home")
        elif ucount>0:
            udata=tbl_user.objects.get(user_email=Email,user_password=Password)
            request.session["uid"]=udata.id
            request.session["uname"]=udata.user_name
            return redirect("User:Home")
        else:
            return render(request,"Guest/Login.html")
    else:
        return render(request,"Guest/Login.html")
