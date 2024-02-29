from django.urls import path,include
from Photographers import views
app_name="Photographers"
urlpatterns = [
    path('Home/',views.Home,name="Home"),

    path('Myprofile/',views.Myprofile,name="Myprofile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('Changpassword/',views.Changpassword,name="Changpassword"),

    path('Post/',views.Post,name="Post"),
    path('Deletepost/<int:did>',views.Deletepost,name="Deletepost"),
    path('Addgallery/<int:gid>',views.Addgallery,name="Addgallery"),
    path('Deletegallery/<int:did>',views.Deletegallery,name="Deletegallery"),

    path('SearchEditor/',views.SearchEditor,name="SearchEditor"),
    path('Ajaxeditorsearch/',views.Ajaxeditorsearch,name="Ajaxeditorsearch"),
    path('Viewmore/<int:eid>',views.Viewmore,name="Viewmore"),
    path('Viewgallery/<int:gid>',views.Viewgallery,name="Viewgallery"),
    path('EditorBooking/<int:eid>',views.EditorBooking,name="EditorBooking"),
    path('ViewEditorBooking/',views.ViewEditorBooking,name="ViewEditorBooking"),

    path('SearchModel/',views.SearchModel,name="SearchModel"),
    path('Ajaxsearchmodel/',views.Ajaxsearchmodel,name="Ajaxsearchmodel"),
    path('Viewmodelpost/<int:pid>',views.Viewmodelpost,name="Viewmodelpost"),
    path('ModelBooking/<int:mid>',views.ModelBooking,name="ModelBooking"),
    path('ViewModelBooking/',views.ViewModelBooking,name="ViewModelBooking"),

    path('ViewUserBooking/',views.ViewUserBooking,name="ViewUserBooking"),
    path('accept/<int:aid>',views.accept,name="accept"),
    path('reject/<int:rid>',views.reject,name="reject"),
    path('AcceptedBooking/',views.AcceptedBooking,name="AcceptedBooking"),
    path('RejectedBooking/',views.RejectedBooking,name="RejectedBooking"),
    
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('echatpage/<int:id>',views.echatpage,name="echatpage"),
    path('ajaxechat/',views.ajaxechat,name="ajaxechat"),
    path('ajaxechatview/',views.ajaxechatview,name="ajaxechatview"),
    path('eclearchat/',views.eclearchat,name="eclearchat"),

    path('mchatpage/<int:id>',views.mchatpage,name="mchatpage"),
    path('ajaxmchat/',views.ajaxmchat,name="ajaxmchat"),
    path('ajaxmchatview/',views.ajaxmchatview,name="ajaxmchatview"),
    path('mclearchat/',views.mclearchat,name="mclearchat"),

    # path('logout/',views.logout,name="logout"),
]

