from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return f'{self.name} - {self.email}'
    

class Service(models.Model):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Team(models.Model):
    member = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teams', null=True,blank=True)
    position = models.CharField(max_length=50)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"
    

class Quote(models.Model):
    departure_city = models.CharField(max_length=50)
    delivery_city = models.CharField(max_length=50)
    weighht = models.PositiveIntegerField(default=0)
    dimension = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    