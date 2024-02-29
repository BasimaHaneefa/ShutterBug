from django.urls import path,include
from Editors import views
app_name="Editors"
urlpatterns = [
    path('Home/',views.Home,name="Home"),
    
    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('Changpassword/',views.Changpassword,name="Changpassword"),

    path('Post/',views.Post,name="Post"),
    path('Deletepost/<int:did>',views.Deletepost,name="Deletepost"),
    path('Addgallery/<int:gid>',views.Addgallery,name="Addgallery"),
    path('Deletegallery/<int:did>',views.Deletegallery,name="Deletegallery"),

    path('ViewPhotogarpherBooking/',views.ViewPhotogarpherBooking,name="ViewPhotogarpherBooking"),
    path('accept/<int:aid>',views.accept,name="accept"),
    path('reject/<int:rid>',views.reject,name="reject"),
    path('AcceptedBooking/',views.AcceptedBooking,name="AcceptedBooking"),
    path('RejectedBooking/',views.RejectedBooking,name="RejectedBooking"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),


]
