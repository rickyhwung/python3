from django.db import models

# Create your models here.
class Bbsuser(models.Model):
    username = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    email = models.EmailField()
    isadmin = models.BooleanField()
class Section(models.Model):
    secname = models.CharField(max_length=50)
    detail = models.TextField()
class Bbspost(models.Model):
    postname = models.CharField(max_length=50)
    uid = models.IntegerField()
    content = models.TextField()
    secid = models.IntegerField()
class Comment(models.Model):
    uid = models.IntegerField()
    comment = models.TextField()
    postid = models.IntegerField()
    pcid = models.IntegerField()