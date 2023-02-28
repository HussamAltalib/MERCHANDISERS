from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#creating a profile for the user
class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    profile_image = models.ImageField( upload_to='profile_pics/', default='profile_pics/default.png')
    user_score = models.IntegerField(default=0)
    about = models.TextField()
    
   


