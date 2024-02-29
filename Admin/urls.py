from django.urls import path
from Admin import views

app_name="Admin"
urlpatterns = [
    
    path('Home/',views.Home,name="Home"),

    path('District/',views.districtInsertSelect,name="districtInsertSelect"),
    path('deletedistrict/<int:id>',views.deletedistrict,name="deletedistrict"),
    path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),

    path('Place/',views.placeInsertSelect,name="placeInsertSelect"),
    path('deleteplace/<int:id>',views.deleteplace,name="deleteplace"),
    path('editplace/<int:id>',views.editplace,name="editplace"),


    path('Category/',views.categoryInsertSelect,name="categoryInsertSelect"),
    path('deletecategory/<int:id>',views.deletecategory,name="deletecategory"),
    path('editcategory/<int:id>',views.editcategory,name="editcategory"),


    path('EditorCategory/',views.edcategoryInsertSelect,name="edcategoryInsertSelect"),
    path('deleteedcategory/<int:id>',views.deleteedcategory,name="deleteedcategory"),
    path('editeditorcategory/<int:id>',views.editeditorcategory,name="editeditorcategory"),

    path('newphotographerverify/',views.newphotographerverify,name="newphotographerverify"),
    path('accept/<int:aid>',views.accept,name="accept"),
    path('reject/<int:rid>',views.reject,name="reject"),
    path('Acceptedphotographer/',views.Acceptedphotographer,name="Acceptedphotographer"),
    path('Rejectedphotographer/',views.Rejectedphotographer,name="Rejectedphotographer"),


    path('neweditorverify/',views.neweditorverify,name="neweditorverify"),
    path('eaccept/<int:aid>',views.eaccept,name="eaccept"),
    path('ereject/<int:rid>',views.ereject,name="ereject"),
    path('Acceptededitor/',views.Acceptededitor,name="Acceptededitor"),
    path('Rejectededitor/',views.Rejectededitor,name="Rejectededitor"),


    path('newmodelverify/',views.newmodelverify,name="newmodelverify"),
    path('maccept/<int:aid>',views.maccept,name="maccept"),
    path('mreject/<int:rid>',views.mreject,name="mreject"),
    path('Acceptedmodel/',views.Acceptedmodel,name="Acceptedmodel"),
    path('Rejectedmodel/',views.Rejectedmodel,name="Rejectedmodel"),

    path('viewcomplaint/',views.ViewComplaint,name="viewcomplaint"),
    path('reply/<int:cid>',views.Reply,name="reply"),
    
    path('viewfeedback/',views.ViewFeedback,name="viewfeedback"),


]
