from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import get_slug
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models import Q
from cloudinary.models import CloudinaryField




class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))
        print(qs)
        print("#########")

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        print("#########")

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print("#########")
        return available
        

    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles


# Create your models here.
class Profile(models.Model):
    first_name=models.CharField(max_length=200, blank=False)
    last_name=models.CharField(max_length=200, blank=False)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.CharField(max_length=350, default="No bio...")
    email=models.EmailField(max_length=200, blank=False)
    avatar =CloudinaryField('image', default="https://res.cloudinary.com/dpcrhvllf/image/upload/v1606208498/ouao15vmh1c1wecxm5ir.png")
    friends=models.ManyToManyField(User, blank=True, related_name='followers')
    created=models.DateTimeField(auto_now_add=True)
    slug= models.SlugField(unique=True, blank=True)


    def __str__(self):
        return f"{self.user.username}-{self.created.strftime('%d-%m-%Y')}"

    objects = ProfileManager()

    def get_friends(self):
        return self.friends.all()

    def friends_no(self):
        return self.friends.all().count
    
    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def get_posts_no(self):
        return self.posts.all().count()

    def get_all_authors_posts(self):
        return self.posts.all()

    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked += 1
        return total_liked

    def get_likes_recieved_no(self):
        posts = self.posts.all()
        total_liked = 0
        for item in posts:
            total_liked += item.liked.all().count()
        return total_liked


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


class RelationshipManager(models.Manager):
    def invatations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
        
