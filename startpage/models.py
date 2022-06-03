from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Muser(models.Model):
    muser = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    status = models.IntegerField(default = 0)

    def __str__(self):
        return self.muser.username





class Contact(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=200)
    message=models.TextField(max_length=400)

    def __str__(self):
        return self.firstname

class Shops(models.Model):
    username= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    ownername= models.CharField(max_length=200)
    shop_name=models.CharField(max_length=200)
    address=models.CharField(max_length=200,null=True)
    whatsapp_no=models.BigIntegerField(default=0)
    status=models.IntegerField(default=0)
    hdstatus=models.CharField(max_length=200,null=True)
    shop_registration = models.FileField(upload_to='vehichle registration',default='')
    shop_photo = models.ImageField(upload_to='vehichle images',default='')
    
    def __str__(self):
        return self.ownername