from django.urls import path,include
from Models import views
app_name="Models"
urlpatterns = [
    path('Home/',views.Home,name="Home"),

    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('Changpassword/',views.Changpassword,name="Changpassword"),

    path('Modelpost/',views.Modelpost,name="Modelpost"),
    path('Deletemodelpost/<int:did>',views.Deletemodelpost,name="Deletemodelpost"),

    path('ViewPhotographerBooking/',views.ViewPhotographerBooking,name="ViewPhotographerBooking"),
    path('accept/<int:aid>',views.accept,name="accept"),
    path('reject/<int:rid>',views.reject,name="reject"),
    path('AcceptedBooking/',views.AcceptedBooking,name="AcceptedBooking"),
    path('RejectedBooking/',views.RejectedBooking,name="RejectedBooking"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

]
