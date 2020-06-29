from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    CATEGORY_CHOICES=[('A','Author'),('R','Reader')]
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=10)
    image=models.ImageField(upload_to='account/',blank=True)
    bio=models.TextField(blank=True)
    category=models.CharField(choices=CATEGORY_CHOICES,default="R",max_length=1)

    REQUIRED_FIELDS=('email','category','first_name','last_name',)

    def __str__(self):
        return self.username