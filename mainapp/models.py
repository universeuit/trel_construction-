from django.db import models

# Create your models here.
class Slidermodel(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=500)
    background_image = models.ImageField(upload_to='slider_image')

class Weoffer(models.Model):
    heading = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    image = models.ImageField(upload_to='weoffer')

class Gallery(models.Model):
    According = (
        ('month','month'),
        ('year','year'),
    )
    image = models.ImageField(upload_to='gallery')
    title = models.CharField(max_length=200)
    price = models.FloatField()
    according = models.CharField(max_length=100, choices=According)

class Project(models.Model):
    According = (
        ('month','month'),
        ('year','year'),
    )
    image = models.ImageField(upload_to='project')
    street_location = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price = models.FloatField()
    according = models.CharField(max_length=100, choices=According)
    description = models.CharField(max_length=500)

class Ourteam(models.Model):
    image = models.ImageField(upload_to='ourteam')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=50)

class Latesnews(models.Model):
    image = models.ImageField(upload_to='latesnews')
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)








