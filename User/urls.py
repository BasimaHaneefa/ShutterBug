from django.urls import path,include
from User import views
app_name="User"
urlpatterns = [
    path('Home/',views.Home,name="Home"),

    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('Changpassword/',views.Changpassword,name="Changpassword"),

    path('SearchPhotographer/',views.SearchPhotographer,name="SearchPhotographer"),
    path('Ajaxsearch/',views.Ajaxsearch,name="Ajaxsearch"),
    path('Viewpost/<int:pid>',views.Viewpost,name="Viewpost"),
    path('Viewgallery/<int:gid>',views.Viewgallery,name="Viewgallery"),
    path('PhotographerBooking/<int:pid>',views.PhotographerBooking,name="PhotographerBooking"),
    path('ViewPhotographerBooking/',views.ViewPhotographerBooking,name="ViewPhotographerBooking"),

    path('complaint/',views.Complaint,name="complaint"),
    path('delcomplaint/<int:did>',views.DelComplaint,name="DeleteComplaint"),
    path('editcomplaint/<int:eid>',views.EditComplaint,name="EditComplaint"),
    
    path('feedback/',views.Feedback,name="feedback"),
    path('delfeedback/<int:did>',views.DelFeedback,name="DeleteFeedback"),
    path('editfeedback/<int:eid>',views.EditFeedback,name="EditFeedback"),

    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    # path('logout/',views.logout,name="logout"),

]
