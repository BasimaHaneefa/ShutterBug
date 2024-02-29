from django.urls import path,include
from Guest import views
app_name="Guest"
urlpatterns = [
    path('',views.index,name="index"),

    path('PhotographerReg/',views.PhotographerReg,name="PhotographerReg"),

    path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),

    path('EditorReg/',views.EditorReg,name="EditorReg"),

    path('ModelReg/',views.ModelReg,name="ModelReg"),

    path('UserReg/',views.UserReg,name="UserReg"),

    path('Login/',views.Login,name="Login"),



]
