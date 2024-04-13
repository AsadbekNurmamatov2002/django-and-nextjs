from django.db import models
from django.utils import timezone
# Create your models here.



class Post(models.Model):
    class Status(models.TextChoices):
        NASHIR='NSh', 'Nashir'
        QORALAMA='QOR','Qoralama'
        
    name=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250, blank=True)
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updtaed=models.DateTimeField(auto_now=True)
    publish=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=3, choices=Status.choices, default=Status.QORALAMA)
    
    def __str__(self) -> str:
        return self.name
    
    
    
    
    