from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import get_slug
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Create your models here.

# Create your models here.
class Profile(models.Model):
    first_name=models.CharField(max_length=200, blank=False)
    last_name=models.CharField(max_length=200, blank=False)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.CharField(max_length=350, default="No bio...")
    email=models.EmailField(max_length=200, blank=False)
    avatar=models.ImageField(default='media/avater.png', upload_to='media/avatar/')
    friends=models.ManyToManyField(User, blank=True, related_name='followers')
    created=models.DateTimeField(auto_now_add=True)
    slug= models.SlugField(unique=True, blank=True)
    

    def get_friends(self):
        return self.friends.all()

    def friends_no(self):
        return self.friends.all().count
    
    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"


    def save(self, *args, **kwargs):
        ex = False
        if self.first_name and self.last_name:
            to_slug = slugify(str(self.first_name)+ " "+str(self.last_name))
            ex = Profile.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug=slugify(to_slug + " "+ str(get_slug()))
                ex = Profile.objects.filter(slug=to_slug).exists()

            else:
                to_slug= str(self.user)
            self.slug = to_slug
            super().save(*args, **kwargs)


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
        
