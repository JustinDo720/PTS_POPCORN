from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_photo = models.ImageField(upload_to='user_profile_pictures/', default='default_profile_pic.jpg')
    user_email = models.EmailField(max_length=254)
    user_bio = models.TextField()

    def __str__(self):
        return f'{self.user.username}'


class Post(models.Model):
    # The owner will be the user who posted the post and owner_profile refers to where they could see their user_photo
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    owner_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False, blank=False)
    comments = models.TextField()
    remain_anonymous = models.BooleanField(default=False)
    picture = models.ImageField(default=None, upload_to='uploaded_img/', blank=True)
    date_of_entry = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comments}'



