from django.db import models
from Admin.models import *
# Create your models here.

class tbl_photographer(models.Model):
    photographer_name=models.CharField(max_length=50)
    photographer_email=models.CharField(max_length=50)
    photographer_contact=models.CharField(max_length=50)
    photographer_address=models.CharField(max_length=100)
    photographer_gender=models.CharField(max_length=50)
    pcat=models.ForeignKey(tbl_photographercategory,on_delete=models.CASCADE)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    photographer_password=models.CharField(max_length=50)
    photographer_photo=models.FileField(upload_to='PhotographerDocs/')
    photographer_proof=models.FileField(upload_to='PhotographerDocs/')
    photographer_vstatus=models.CharField(max_length=10,default=0)
    photographer_doj=models.DateField(auto_now_add=True)


class tbl_editor(models.Model):
    editor_name=models.CharField(max_length=50)
    editor_email=models.CharField(max_length=50)
    editor_contact=models.CharField(max_length=50)
    editor_address=models.CharField(max_length=100)
    editor_gender=models.CharField(max_length=50)
    ecat=models.ForeignKey(tbl_editorcategory,on_delete=models.CASCADE)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    editor_password=models.CharField(max_length=50)
    editor_photo=models.FileField(upload_to='EditorDocs/')
    editor_proof=models.FileField(upload_to='EditorDocs/')
    editor_vstatus=models.CharField(max_length=10,default=0)
    editor_doj=models.DateField(auto_now_add=True)


class tbl_model(models.Model):
    model_name=models.CharField(max_length=50)
    model_email=models.CharField(max_length=50)
    model_contact=models.CharField(max_length=50)
    model_address=models.CharField(max_length=100)
    model_gender=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    model_password=models.CharField(max_length=50)
    model_photo=models.FileField(upload_to='ModelDocs/')
    model_proof=models.FileField(upload_to='ModelDocs/')
    model_vstatus=models.CharField(max_length=10,default=0)
    model_doj=models.DateField(auto_now_add=True)

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_address=models.CharField(max_length=100)
    user_gender=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_password=models.CharField(max_length=50)
    user_photo=models.FileField(upload_to='UserDocs/')
    user_doj=models.DateField(auto_now_add=True)