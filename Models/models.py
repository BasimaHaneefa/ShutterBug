from django.db import models
from Guest.models import tbl_model, tbl_photographer
# Create your models here.

class tbl_modelpic(models.Model):
    post_image=models.FileField(upload_to='Modelpics/')
    post_caption=models.CharField(max_length=100)
    model=models.ForeignKey(tbl_model,on_delete=models.CASCADE)

class tbl_mchat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    model_from = models.ForeignKey(tbl_model,on_delete=models.CASCADE,related_name="model_from",null=True)
    model_to = models.ForeignKey(tbl_model,on_delete=models.CASCADE,related_name="model_to",null=True)
    photographer_from=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE,related_name="photographer_receiveid",null=True)
    photographer_to=models.ForeignKey(tbl_photographer,on_delete=models.CASCADE,related_name="photographer_sentid",null=True)
