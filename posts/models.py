from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    catName=models.CharField(max_length=20)
    catDesc=models.TextField()
    def getPosts(self):
        return self.post_set
   
    def __str__(self):
        return self.catName
  

class Post(models.Model):
    title=models.CharField(max_length=20)
    content=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    text=models.TextField()
    cdata=models.DateField(auto_now=False)
    visible=models.BooleanField()

class Location(models.Model):
    name=models.TextField()

    class Meta:
     db_table='ABCDE'


class Page(models.Model):
    name=models.CharField(max_length=20)
    location=models.ManyToManyField(Location)



   