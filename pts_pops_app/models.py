from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to='user_profile_pictures/', default='default_profile_pic.jpg')

    def __str__(self):
        return f'{user.username}'


class Post(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comments = models.TextField()
    remain_anonymous = models.BooleanField(default=False)
    picture = models.ImageField(default=None, upload_to='uploaded_img/', blank=True)
    date_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comments}'



