from django.db import models
from Guest.models import tbl_photographer,tbl_user
# Create your models here.
class  tbl_booking(models.Model):
    photographer=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_date=models.DateField(auto_now_add=True)
    payment_status=models.CharField(max_length=10,default=0)
    payment_amount=models.CharField(max_length=50,default=0)
    booking_description=models.CharField(max_length=100)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    booking_vstatus=models.CharField(max_length=10,default=0)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=100)
    complaint_status=models.CharField(default=0,max_length=5)
    complaint_reply=models.CharField(default="Not replied yet",max_length=100)
    complaint_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_uchat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    photographer_from=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE,related_name="photographer_recieved",null=True)
    photographer_to=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE,related_name="photographer_sent",null=True)
