from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)  
    description = models.TextField()
    technology=models.CharField(max_length=200,null=True,blank=True)
    created_add=models.DateTimeField(auto_now_add=True)
    
    