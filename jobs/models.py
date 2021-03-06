from django.db import models

# Create your models here.
class Job(models.Model):
    #title
    title = models.CharField(max_length=100)
    #image
    image = models.ImageField(upload_to='images/')
    #summary
    summary = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title