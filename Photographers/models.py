from django.db import models
from Guest.models import tbl_photographer,tbl_editor,tbl_model
# Create your models here.

class tbl_post(models.Model):
    post_name=models.CharField(max_length=50)
    post_image=models.FileField(upload_to='PostDocs/')
    post_caption=models.CharField(max_length=100)
    post_amount=models.CharField(max_length=100)
    paid_status=models.CharField(max_length=10,default=0)
    p_status=models.CharField(max_length=10,default=0)
    photographer=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE,null=True)
    editor=models.ForeignKey(tbl_editor,on_delete=models.CASCADE,null=True)

class tbl_addgallery(models.Model):
    addgallery_caption=models.CharField(max_length=100)
    addgallery_image=models.FileField(upload_to='GalleryDocs/')
    post=models.ForeignKey(tbl_post,on_delete=models.CASCADE)
    p_status=models.CharField(max_length=10,default=0)

class tbl_ebooking(models.Model):
    editor=models.ForeignKey(tbl_editor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_date=models.DateField(auto_now_add=True)
    payment_status=models.CharField(default=0,max_length=10)
    payment_amount=models.IntegerField(default=0)
    ebooking_discription=models.CharField(max_length=100)
    photographer=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE)
    ebooking_vstatus=models.CharField(default=0,max_length=10)

class tbl_mbooking(models.Model):
    model=models.ForeignKey(tbl_model,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_date=models.DateField(auto_now_add=True)
    payment_status=models.CharField(max_length=10,default=0)
    payment_amount=models.CharField(max_length=10,default=0)
    mbooking_discription=models.CharField(max_length=10)
    photographer=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE)
    mbooking_vstatus=models.CharField(max_length=10,default=0)

class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    editor_from = models.ForeignKey(tbl_editor,on_delete=models.CASCADE,related_name="editor_from",null=True)
    editor_to = models.ForeignKey(tbl_editor,on_delete=models.CASCADE,related_name="editor_to",null=True)
    photographer_from=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE,related_name="photographer_from",null=True)
    photographer_to=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE,related_name="photographer_to",null=True)
