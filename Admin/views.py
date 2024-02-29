from django.shortcuts import redirect, render
from Admin.models import *
from Guest.models import tbl_photographer,tbl_editor,tbl_model, tbl_user
from User.models import tbl_complaint, tbl_feedback
# Create your views here.
#####################HomePage######################################

def Home(request):
    if 'adid' in request.session:
        tphotographer=tbl_photographer.objects.filter(photographer_vstatus=1).count()
        teditor=tbl_editor.objects.filter(editor_vstatus=1).count()
        tmodel=tbl_model.objects.filter(model_vstatus=1).count()
        tuser=tbl_user.objects.all().count()
        return render(request,"Admin/HomePage.html",{'count1':tphotographer,'count2':teditor,'count3':tmodel,'count4':tuser})
    else:
        return render(request,"Guest/Login.html")

#####################District#######################################
def districtInsertSelect(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtdistrict')
        tbl_district.objects.create(district_name=disName)
        return render(request,"Admin/District.html",{'data':dis})
    else:
        return render(request,"Admin/District.html",{'data':dis})
    
def deletedistrict(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:districtInsertSelect")

def editdistrict(request,id):
    edis=tbl_district.objects.get(id=id)
    if request.method=="POST":
        edis.district_name=request.POST.get('txtdistrict')
        edis.save()
        return redirect("Admin:districtInsertSelect")
    else:
        return render(request,"Admin/District.html",{'edis':edis})

############################Place#################################

def placeInsertSelect(request):
    dis=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        seldis=tbl_district.objects.get(id=request.POST.get("sel_dist"))
        placeName=request.POST.get('txtplace')
        tbl_place.objects.create(place_name=placeName,district=seldis)
        return render(request,"Admin/Place.html",{'data':place,'district':dis})
    else:
        return render(request,"Admin/Place.html",{'data':place,'district':dis})

def deleteplace(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:placeInsertSelect")

def editplace(request,id):
    dist=tbl_district.objects.all()
    edis=tbl_place.objects.get(id=id)
    if request.method=="POST":
        dis=tbl_district.objects.get(id=request.POST.get("sel_dist"))
        edis.district=dis
        edis.place_name=request.POST.get('txtplace')
        edis.save()
        return redirect("Admin:placeInsertSelect")
    else:
        return render(request,"Admin/Place.html",{'edis':edis,'district':dist})

##########################PhotographerCategory#################################

def categoryInsertSelect(request):
    pcat=tbl_photographercategory.objects.all()
    if request.method=="POST":
        pcategory=request.POST.get('txtcategory')
        tbl_photographercategory.objects.create(pcat_name=pcategory)
        return render(request,"Admin/PhotographerCategory.html",{'data':pcat})
    else:
        return render(request,"Admin/PhotographerCategory.html",{'data':pcat})

def deletecategory(request,id):
    tbl_photographercategory.objects.get(id=id).delete()
    return redirect("Admin:categoryInsertSelect")

def editcategory(request,id):
    edis=tbl_photographercategory.objects.get(id=id)
    if request.method=="POST":
        edis.pcat_name=request.POST.get('txtcategory')
        edis.save()
        return redirect("Admin:categoryInsertSelect")
    else:
        return render(request,"Admin/PhotographerCategory.html",{'edis':edis})

#########################Editorcategory#########################################

def edcategoryInsertSelect(request):
    ecat=tbl_editorcategory.objects.all()
    if request.method=="POST":
        ecategory=request.POST.get('txtedcategory')
        tbl_editorcategory.objects.create(ecat_name=ecategory)
        return render(request,"Admin/EditorCategory.html",{'data':ecat})
    else:
        return render(request,"Admin/EditorCategory.html",{'data':ecat})

def deleteedcategory(request,id):
    tbl_editorcategory.objects.get(id=id).delete()
    return redirect("Admin:edcategoryInsertSelect")

def editeditorcategory(request,id):
    edis=tbl_editorcategory.objects.get(id=id)
    if request.method=="POST":
        edis.ecat_name=request.POST.get('txtedcategory')
        edis.save()
        return redirect("Admin:edcategoryInsertSelect")
    else:
        return render(request,"Admin/EditorCategory.html",{'edis':edis})

###########################PhotographerVerify############################
    
def newphotographerverify(request):
    newdata=tbl_photographer.objects.filter(photographer_vstatus=0)
    return render(request,"Admin/PhotographerVerification.html",{"new":newdata})

def accept(request,aid):
    acc=tbl_photographer.objects.get(id=aid)
    acc.photographer_vstatus=1
    acc.save()
    return redirect("Admin:newphotographerverify")

def reject(request,rid):
    rej=tbl_photographer.objects.get(id=rid)
    rej.photographer_vstatus=2
    rej.save()
    return redirect("Admin:newphotographerverify")

def Acceptedphotographer(request):
    accdata=tbl_photographer.objects.filter(photographer_vstatus=1)
    return render(request,"Admin/AcceptedPhotographer.html",{"acc":accdata})

def Rejectedphotographer(request):
    rejdata=tbl_photographer.objects.filter(photographer_vstatus=2)
    return render(request,"Admin/RejectedPhotographer.html",{"rej":rejdata})

############################EditorVerify#################################

def neweditorverify(request):
    newdata=tbl_editor.objects.filter(editor_vstatus=0)
    return render(request,"Admin/EditorVerification.html",{"new":newdata})

def eaccept(request,aid):
    acc=tbl_editor.objects.get(id=aid)
    acc.editor_vstatus=1
    acc.save()
    return redirect("Admin:neweditorverify")

def ereject(request,rid):
    rej=tbl_editor.objects.get(id=rid)
    rej.editor_vstatus=2
    rej.save()
    return redirect("Admin:neweditorverify")

def Acceptededitor(request):
    accdata=tbl_editor.objects.filter(editor_vstatus=1)
    return render(request,"Admin/AcceptedEditor.html",{"acc":accdata})

def Rejectededitor(request):
    rejdata=tbl_editor.objects.filter(editor_vstatus=2)
    return render(request,"Admin/RejectedEditor.html",{"rej":rejdata})

##########################ModelVerify###################################

def newmodelverify(request):
    newdata=tbl_model.objects.filter(model_vstatus=0)
    return render(request,"Admin/ModelVerification.html",{"new":newdata})

def maccept(request,aid):
    acc=tbl_model.objects.get(id=aid)
    acc.model_vstatus=1
    acc.save()
    return redirect("Admin:newmodelverify")

def mreject(request,rid):
    rej=tbl_model.objects.get(id=rid)
    rej.model_vstatus=2
    rej.save()
    return redirect("Admin:newmodelverify")

def Acceptedmodel(request):
    accdata=tbl_model.objects.filter(model_vstatus=1)
    return render(request,"Admin/AcceptedModel.html",{"acc":accdata})

def Rejectedmodel(request):
    rejdata=tbl_model.objects.filter(model_vstatus=2)
    return render(request,"Admin/RejectedModel.html",{"rej":rejdata})

#########################ViewComplaint##########################################

def ViewComplaint(request):
    com=tbl_complaint.objects.filter(complaint_status=0)
    replied=tbl_complaint.objects.filter(complaint_status=1)
    return render(request,"Admin/ViewComplaint.html",{"new":com,"replied":replied})

def Reply(request,cid):
    com=tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        com.complaint_reply=request.POST.get("Reply")
        com.complaint_status=1
        com.save()
        return redirect("Admin:viewcomplaint")
    else:
        return render(request,"Admin/Reply.html")    
    
#######################ViewFeedback####################################################

def ViewFeedback(request):
    com=tbl_feedback.objects.all()
    return render(request,"Admin/ViewFeedback.html",{"new":com})