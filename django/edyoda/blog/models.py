from django.db import models
from django.utils.text import slugify
from django.urls import reverse,reverse_lazy
from django.contrib.auth import get_user_model
# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    slug=models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class Post(models.Model):
    statuses=[('D','Draft'),('P','Published')]
    title=models.CharField(max_length=250)
    content=models.TextField()
    status=models.CharField(choices=statuses,default="D", max_length=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image_url=models.CharField(max_length=1000,blank=True)
    author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog/',blank=True)
    date=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique = True, blank=True)

    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    def get_absolute_url(self):         #this is not needed
        return reverse("Blog Details", args=[self.slug])