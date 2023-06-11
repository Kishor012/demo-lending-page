from django.db import models

# Create your models here.


class Advertise(models.Model):
    title = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    website = models.URLField(max_length=50,blank=True)
    webname = models.CharField(max_length=50,blank=True)
    desc = models.TextField(max_length=2500)
   
    subtitleone = models.CharField(max_length=500,blank=True)
    subphotoone = models.ImageField(upload_to="myimage",blank=True)
    subdescone = models.TextField(max_length=2500,blank=True)
    
    subtitletwo = models.CharField(max_length=500,blank=True)
    subphototwo = models.ImageField(upload_to="myimage",blank=True)
    subdesctwo = models.TextField(max_length=2500,blank=True)
    
    subtitlethree = models.CharField(max_length=500,blank=True)
    subphotothree = models.ImageField(upload_to="myimage",blank=True)
    subdescthree = models.TextField(max_length=2500,blank=True)

class Makemoney(models.Model):
    title = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    website = models.URLField(max_length=50,blank=True)
    webname = models.CharField(max_length=50,blank=True)
    desc = models.TextField(max_length=2500)
   
    subtitleone = models.CharField(max_length=500,blank=True)
    subphotoone = models.ImageField(upload_to="myimage",blank=True)
    subdescone = models.TextField(max_length=2500,blank=True)
    
    subtitletwo = models.CharField(max_length=500,blank=True)
    subphototwo = models.ImageField(upload_to="myimage",blank=True)
    subdesctwo = models.TextField(max_length=2500,blank=True)
    
    subtitlethree = models.CharField(max_length=500,blank=True)
    subphotothree = models.ImageField(upload_to="myimage",blank=True)
    subdescthree = models.TextField(max_length=2500,blank=True)


class Technology(models.Model):
    title = models.CharField(max_length=500)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    website = models.URLField(max_length=50, blank=True)
    webname = models.CharField(max_length=50,blank=True)
    desc = models.TextField(max_length=2500)
   
    subtitleone = models.CharField(max_length=500,blank=True)
    subphotoone = models.ImageField(upload_to="myimage",blank=True)
    subdescone = models.TextField(max_length=2500,blank=True)
    
    subtitletwo = models.CharField(max_length=500,blank=True)
    subphototwo = models.ImageField(upload_to="myimage",blank=True)
    subdesctwo = models.TextField(max_length=2500,blank=True)
    
    subtitlethree = models.CharField(max_length=500,blank=True)
    subphotothree = models.ImageField(upload_to="myimage",blank=True)
    subdescthree = models.TextField(max_length=2500,blank=True)

