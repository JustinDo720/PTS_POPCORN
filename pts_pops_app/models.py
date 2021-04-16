from django.db import models
from django.contrib.auth.models import User, AnonymousUser
import os

AWS_BUCKET_BASEURL = 'https://%s.s3.amazonaws.com' % os.environ.get('AWS_STORAGE_BUCKET_NAME')

RATE_CHOICES = (
    ("1", "1 Star: It was okay but you could've done better Justin!!"),
    ("2", "2 Star: It was really decent for a 3 days worth of code"),
    ("3", "3 Star: Nice! This was unexpected!"),

)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to=f'{AWS_BUCKET_BASEURL}/user_profile_pictures/', default='default_profile_pic.jpg')
    user_email = models.EmailField(max_length=254, null=True, help_text='This field is not required!!')
    user_bio = models.TextField(null=True, blank=True, help_text='This field is not required!!')

    def __str__(self):
        return f'{self.user.username}'


class Post(models.Model):
    # The owner will be the user who posted the post and owner_profile refers to where they could see their user_photo
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    owner_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None, null=True)
    comments = models.TextField()
    remain_anonymous = models.BooleanField(default=False)
    picture = models.ImageField(default=None, upload_to=f'{AWS_BUCKET_BASEURL}/uploaded_img/', blank=True)
    date_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comments}'


# Feedback Model
class Feedback(models.Model):
    opinions = models.TextField()
    good = models.CharField(max_length=100, choices=RATE_CHOICES)
    name = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return f'{self.opinions}'