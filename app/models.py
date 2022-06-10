from django.db import models
from datetime import datetime

# Create your models here.
class reg(models.Model):
  fname=models.CharField(max_length=50,default="null")
  lname=models.CharField(max_length=50,default="null")
  uname=models.CharField(max_length=50,default="null")
  phone=models.CharField(max_length=50,default="null")
  gender=models.CharField(max_length=50,default="null")
  answer=models.CharField(max_length=50,default="null")
  password=models.CharField(max_length=50,default="null")
  email=models.CharField(max_length=50,default="null")
  typeo=models.CharField(max_length=50,default="null")
  image=models.ImageField(upload_to='pics',default="null")
 
class cars(models.Model):
  name=models.CharField(max_length=50,default="null")
  start_price=models.IntegerField(max_length=50,default="null")
  end_price=models.IntegerField(max_length=50,default="null")
  millage=models.CharField(max_length=50,default="null")
  cc=models.CharField(max_length=50,default="null")
  type=models.CharField(max_length=50,default="null")
  image=models.ImageField(upload_to='pics',default="null")

class carbook(models.Model):
  carname=models.CharField(max_length=50,default="null")
  username=models.CharField(max_length=50,default="null")
  fname=models.CharField(max_length=50,default="null")
  lname=models.CharField(max_length=50,default="null")
  licence=models.CharField(max_length=50,default="null")
  pickdate=models.CharField(max_length=50,default="null")
  dropdate=models.CharField(max_length=50,default="null")
  location=models.CharField(max_length=100,default="null")
  image=models.ImageField(upload_to='pics',default="null")
  status=models.CharField(max_length=100,default="cancled")

class booked(models.Model):
  username=models.CharField(max_length=50,default="null")
  status=models.CharField(max_length=100,default="null")
  date=models.DateTimeField(default=datetime.now().date())
  time=models.DateTimeField(default=datetime.now().date())

class card(models.Model):
  cardname=models.CharField(max_length=50,default="null")
  cardnumber=models.CharField(max_length=50,default="null")
  carddate=models.CharField(max_length=50,default="null")
  cardcvv=models.CharField(max_length=50,default="null")