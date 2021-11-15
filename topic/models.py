from django.db import models
from django.db.models.base import Model

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)
    closure_date = models.DateTimeField(null=True)
    final_closure_date = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Idea(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=500, null=True)
    file = models.FileField(upload_to='')
    date = models.DateTimeField(null=True)
    

